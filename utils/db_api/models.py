from typing import Dict, Optional

from pretty_utils.type_functions.classes import AutoRepr
from sqlalchemy import (Column, Integer, Text, Boolean, Float)
from sqlalchemy.orm import declarative_base

# --- Wallets
Base = declarative_base()


class Proxy(Base, AutoRepr):
    __tablename__ = 'proxies'

    id = Column(Integer, primary_key=True)
    raw_data = Column(Text)
    ip = Column(Text, unique=True)
    port = Column(Text)
    username = Column(Text)
    password = Column(Text)
    proxy_type = Column(Text)

    def __init__(self, raw_data: str, ip: str, port: str, username: str, password: str, proxy_type: str) -> None:
        self.raw_data = raw_data
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.proxy_type = proxy_type


class IPInfo(Base, AutoRepr):
    __tablename__ = 'ips_info'

    id = Column(Integer, primary_key=True)
    ip = Column(Text, unique=True)
    network = Column(Text)
    version = Column(Text)
    city = Column(Text)
    region = Column(Text)
    region_code = Column(Text)
    country = Column(Text)
    country_name = Column(Text)
    country_code = Column(Text)
    country_code_iso3 = Column(Text)
    country_capital = Column(Text)
    country_tld = Column(Text)
    continent_code = Column(Text)
    in_eu = Column(Boolean)
    postal = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    timezone = Column(Text)
    utc_offset = Column(Text)
    country_calling_code = Column(Text)
    currency = Column(Text)
    currency_name = Column(Text)
    languages = Column(Text)
    country_area = Column(Float)
    country_population = Column(Integer)
    asn = Column(Text)
    org = Column(Text)

    def __init__(self, json_data: Dict[str, Optional[str]]) -> None:
        self.ip = json_data.get('ip')
        self.network = json_data.get('network')
        self.version = json_data.get('version')
        self.city = json_data.get('city')
        self.region = json_data.get('region')
        self.region_code = json_data.get('region_code')
        self.country = json_data.get('country')
        self.country_name = json_data.get('country_name')
        self.country_code = json_data.get('country_code')
        self.country_code_iso3 = json_data.get('country_code_iso3')
        self.country_capital = json_data.get('country_capital')
        self.country_tld = json_data.get('country_tld')
        self.continent_code = json_data.get('continent_code')
        self.in_eu = json_data.get('in_eu')
        self.postal = json_data.get('postal')
        self.latitude = json_data.get('latitude')
        self.longitude = json_data.get('longitude')
        self.timezone = json_data.get('timezone')
        self.utc_offset = json_data.get('utc_offset')
        self.country_calling_code = json_data.get('country_calling_code')
        self.currency = json_data.get('currency')
        self.currency_name = json_data.get('currency_name')
        self.languages = json_data.get('languages')
        self.country_area = json_data.get('country_area')
        self.country_population = json_data.get('country_population')
        self.asn = json_data.get('asn')
        self.org = json_data.get('org')


class ProviderInfo(Base, AutoRepr):
    __tablename__ = 'providers_info'

    id = Column(Integer, primary_key=True)
    ip = Column(Text, unique=True)
    city = Column(Text)
    region = Column(Text)
    country = Column(Text)
    org = Column(Text)
    postal = Column(Text)
    timezone = Column(Text)

    def __init__(self, json_data: Dict[str, Optional[str]]) -> None:
        self.ip = json_data.get('ip')
        self.city = json_data.get('city')
        self.region = json_data.get('region')
        self.country = json_data.get('country')
        self.org = json_data.get('org')
        self.postal = json_data.get('postal')
        self.timezone = json_data.get('timezone')


class SiteAccessibility(Base, AutoRepr):
    __tablename__ = 'sites_accessibility'

    id = Column(Integer, primary_key=True)
    ip = Column(Text)
    site_url = Column(Text)
    successfully = Column(Boolean)

    def __init__(self, ip: str, site_url: str, successfully: bool) -> None:
        self.ip = ip
        self.site_url = site_url
        self.successfully = successfully
