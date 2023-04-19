import asyncio
import logging
from typing import Tuple, Dict

import aiohttp
from aiohttp_socks import ProxyConnector
from colorama import Fore
from pretty_utils.type_functions.lists import split_list

from data.models import Settings
from utils.db_api.database import get_proxies, db
from utils.db_api.models import Proxy, ProviderInfo
from utils.miscellaneous.cprint import cprint


async def parse(sem: asyncio.Semaphore, settings: Settings, proxy: Proxy) -> Tuple[Proxy, Dict[str, str]]:
    for i in range(3):
        try:
            async with sem:
                connector = ProxyConnector.from_url(
                    f'{proxy.proxy_type}://{proxy.username}:{proxy.password}@{proxy.ip}:{proxy.port}'
                )
                async with aiohttp.ClientSession(connector=connector) as session:
                    async with session.get(url='https://ipinfo.io/json', timeout=settings.timeout) as response:
                        status_code = response.status
                        if status_code <= 201:
                            return proxy, await response.json()

        except BaseException as e:
            logging.exception(f'parse | {proxy.ip}')
            if i >= 2:
                return proxy, {'ip': proxy.ip, 'error': str(e)}

            await asyncio.sleep(1)


async def parse_providers_info(settings: Settings) -> None:
    proxy_list = []
    for proxy in get_proxies():
        if not db.one(ProviderInfo, ProviderInfo.ip == proxy.ip):
            proxy_list.append(proxy)

    if proxy_list:
        proxy_lists = split_list(s_list=proxy_list, n=settings.threads)
        sem = asyncio.Semaphore(1000)
        for proxy_list in proxy_lists:
            tasks = []

            for proxy in proxy_list:
                task = asyncio.ensure_future(parse(sem=sem, settings=settings, proxy=proxy))
                tasks.append(task)

            responses = asyncio.gather(*tasks)
            for response in await responses:
                try:
                    proxy, json_data = response
                    db.insert(ProviderInfo(json_data=json_data))
                    if 'error' in json_data:
                        await cprint(text=f'Failed to parse provider info: {json_data["error"]}', color=Fore.RED)

                    else:
                        await cprint(text='Provider info was parsed.', color=Fore.GREEN, proxy=proxy)

                except BaseException as e:
                    logging.exception('parse_providers_info')
                    await cprint(text=f'Failed to parse provider info: {e}', color=Fore.RED)
