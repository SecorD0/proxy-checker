from typing import List

from pretty_utils.miscellaneous.files import read_json
from pretty_utils.type_functions.classes import AutoRepr, Singleton

from data.config import SETTINGS_FILE


class Settings(Singleton, AutoRepr):
    def __init__(self):
        json = read_json(path=SETTINGS_FILE)

        self.threads: int = json['threads']
        self.timeout: int = json['timeout']
        self.proxies_type: str = json['proxies_type']
        self.parse_ip_info: bool = json['parse_ip_info']
        self.parse_provider_info: bool = json['parse_provider_info']
        self.check_accessibility: List[str] = json['check_accessibility']
