from typing import Optional

from pretty_utils.miscellaneous.files import touch, write_json, read_json
from pretty_utils.type_functions.dicts import update_dict

from data import config


def create_files():
    touch(path=config.FILES_DIR)
    touch(path=config.PROXIES_FILE, file=True)

    try:
        current_settings: Optional[dict] = read_json(path=config.SETTINGS_FILE)

    except FileNotFoundError:
        current_settings = {}

    settings = {
        'threads': 20,
        'timeout': 10,
        'proxies_type': 'http',
        'parse_ip_info': True,
        'parse_provider_info': True,
        'check_accessibility': [
            'https://google.com/',
            'https://twitter.com/',
            'https://facebook.com/',
            'https://www.linkedin.com/'
        ]
    }
    write_json(path=config.SETTINGS_FILE, obj=update_dict(modifiable=current_settings, template=settings), indent=2)


create_files()
