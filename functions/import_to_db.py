import logging
from typing import List

from colorama import Fore

from data.models import Settings
from utils.db_api.database import db, get_proxy
from utils.db_api.models import Proxy
from utils.miscellaneous.cprint import cprint


async def import_to_db(settings: Settings, proxies: List[str]) -> None:
    for proxy in proxies:
        try:
            if '@' in proxy:
                username_and_password, ip_and_port = proxy.split('@')
                username, password = username_and_password.split(':')
                ip, port = ip_and_port.split(':')

            else:
                ip, port, username, password = proxy.split(':')

            proxy_instance = get_proxy(ip=ip)
            if proxy_instance:
                proxy_instance.ip = ip
                proxy_instance.port = port
                proxy_instance.username = username
                proxy_instance.password = password
                await cprint(text='Successfully edited.', color=Fore.GREEN, proxy=proxy_instance)

            else:
                proxy_instance = Proxy(
                    raw_data=proxy, ip=ip, port=port, username=username, password=password,
                    proxy_type=settings.proxies_type
                )
                db.insert(proxy_instance)
                await cprint(text='Successfully imported.', color=Fore.GREEN, proxy=proxy_instance)

        except BaseException as e:
            logging.exception('import_to_db')
            await cprint(text=f'{proxy} | Failed to import proxy: {e}', color=Fore.RED)
