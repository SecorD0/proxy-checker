import asyncio
import logging
from itertools import product
from typing import Tuple

import aiohttp
from aiohttp_socks import ProxyConnector
from colorama import Fore
from pretty_utils.type_functions.lists import split_list

from data.models import Settings
from utils.db_api.database import get_proxies, db
from utils.db_api.models import Proxy, SiteAccessibility
from utils.miscellaneous.cprint import cprint


async def check(sem: asyncio.Semaphore, settings: Settings, proxy: Proxy,
                site_url: str) -> Tuple[Proxy, str, bool]:
    for i in range(3):
        try:
            async with sem:
                connector = ProxyConnector.from_url(
                    f'{proxy.proxy_type}://{proxy.username}:{proxy.password}@{proxy.ip}:{proxy.port}'
                )
                async with aiohttp.ClientSession(connector=connector) as session:
                    async with session.get(url=site_url, timeout=settings.timeout) as response:
                        status_code = response.status
                        if status_code <= 201:
                            return proxy, site_url, True

        except asyncio.exceptions.TimeoutError:
            return proxy, site_url, False

        except:
            logging.exception(f'check | {proxy.ip}')
            await asyncio.sleep(1)

    return proxy, site_url, False


async def check_sites_accessibility(settings: Settings) -> None:
    site_list = []
    for proxy, site_url in product(get_proxies(), settings.check_accessibility):
        if not db.one(
                SiteAccessibility, (SiteAccessibility.ip == proxy.ip) & (SiteAccessibility.site_url == site_url)
        ):
            site_list.append((proxy, site_url))

    if site_list:
        site_lists = split_list(s_list=site_list, n=settings.threads)
        sem = asyncio.Semaphore(1000)
        for site_list in site_lists:
            tasks = []

            for proxy, site_url in site_list:
                task = asyncio.ensure_future(check(sem=sem, settings=settings, proxy=proxy, site_url=site_url))
                tasks.append(task)

            responses = asyncio.gather(*tasks)
            for response in await responses:
                try:
                    proxy, site_url, successfully = response
                    db.insert(SiteAccessibility(ip=proxy.ip, site_url=site_url, successfully=successfully))
                    if successfully:
                        await cprint(text=f'{site_url} is available.', color=Fore.GREEN, proxy=proxy)

                    else:
                        await cprint(text=f"{site_url} isn't available.", color=Fore.RED, proxy=proxy)

                except BaseException as e:
                    logging.exception('check_sites_accessibility')
                    await cprint(text=f'Failed to parse provider info: {e}', color=Fore.RED)
