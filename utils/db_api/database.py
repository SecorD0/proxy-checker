from typing import List, Optional

from pretty_utils.databases import sqlalchemy_

from utils.db_api.models import Base, Proxy


# --- Functions
def get_proxy(ip: str) -> Optional[Proxy]:
    return db.one(Proxy, Proxy.ip == ip)


def get_proxies() -> List[Proxy]:
    return db.all(Proxy)


# --- Miscellaneous
db = sqlalchemy_.DB('sqlite:///files/temp.db', pool_recycle=3600, connect_args={'check_same_thread': False})

db.create_tables(Base)
