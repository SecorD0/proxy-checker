import asyncio
import platform
from typing import List

from colorama import Fore, Style
from pretty_utils.miscellaneous.files import read_lines

from utils.miscellaneous.create_files import create_files
from data.config import PROXIES_FILE
from data.models import Settings
from functions.check_sites_accessibility import check_sites_accessibility
from functions.export_to_spreadsheet import export_to_spreadsheet
from functions.import_to_db import import_to_db
from functions.parse_ips_info import parse_ips_info
from functions.parse_providers_info import parse_providers_info
from utils.miscellaneous.cprint import cprint


async def main(proxies: List[str]):
    settings = Settings()
    if proxies:
        if settings.proxies_type not in ('http', 'socks5'):
            await cprint(
                text="The value of the 'proxies_type' setting must be either 'http' or 'socks5'!", color=Fore.RED
            )
            return

        if not any((settings.parse_ip_info, settings.parse_provider_info, settings.check_accessibility)):
            await cprint(text='Set up actions performed on the proxy!', color=Fore.RED)
            return

        await cprint(text='Importing proxies into a temporary database.', color=Fore.GREEN)
        await import_to_db(settings=settings, proxies=proxies)

        if settings.parse_ip_info:
            await cprint(text='IP info parsing.', color=Fore.GREEN)
            await parse_ips_info(settings=settings)

        if settings.parse_provider_info:
            await cprint(text='Provider info parsing.', color=Fore.GREEN)
            await parse_providers_info(settings=settings)

        if settings.check_accessibility:
            await cprint(text='Sites accessibility checking.', color=Fore.GREEN)
            await check_sites_accessibility(settings=settings)

        await export_to_spreadsheet()

    else:
        text = 'There are no proxies in the proxies.txt file!' if platform.system() == 'Windows' else \
            f'{Fore.RED}There are no proxies in the proxies.txt file!{Style.RESET_ALL}'
        print(text)


if __name__ == '__main__':
    create_files()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main(proxies=read_lines(path=PROXIES_FILE, skip_empty_rows=True)))
    text = '\nPress Enter to exit.\n' if platform.system() == 'Windows' else \
        f'\nPress {Fore.LIGHTGREEN_EX}Enter{Style.RESET_ALL} to exit.\n'
    input(text)
