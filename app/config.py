import os
from decimal import Decimal
from pydantic import BaseSettings

THIS_DIR = os.path.dirname(__file__)

# A degree of longitude:
# at the equator (widest) - around 111 km
# at 40 degrees north and south - around 85 km

# We can take a rough 100 km per degree as most of World's Population
# lives in 60 degrees north and 30 degrees south

# Examples of accuracy values:
# 0.01 - approximate coordinates by ~1 km
# 0.02 - approximate coordinates by ~2 km
# 1.0 - approximate coordinates by ~100 km


class Config(BaseSettings):
    """These variables are overwritten by environment variables"""
    database_url: str = f"sqlite:///{THIS_DIR}/db.sqlite"
    test_database_url: str = f"sqlite:///{THIS_DIR}/db_test.sqlite"
    token: str = "my-super-secret-token"  # emulate authentication
    accuracy: Decimal = Decimal("0.01")  # set value in degrees


settings = Config()
