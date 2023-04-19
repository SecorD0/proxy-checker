import platform
from typing import Optional

from colorama import Style
from pretty_utils.miscellaneous.time_and_date import unix_to_strtime

from utils.db_api.models import Proxy


async def cprint(text: str, color: Optional[str] = '', proxy: Optional[Proxy] = None) -> None:
    printable_text = f'{unix_to_strtime()}'
    if proxy:
        printable_text += f' | {proxy.ip}:{proxy.port}'

    printable_text += f' | {text}'
    if platform.system() == 'Windows':
        print(printable_text)

    else:
        print(color + printable_text + Style.RESET_ALL)
