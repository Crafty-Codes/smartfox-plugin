from .data import SmartfoxData
from homeassistant.const import (
    UnitOfPower
)

DOMAIN = "smartfox"
NAME = DOMAIN
CONF_HOST = "host"

DEFAULT_HOST = "http://smartfox/values.xml"

SENSORS = [
    SmartfoxData(
        name="To Grid",
        key="toGridValue",
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        change=changerToGrid
    )
]

def changerToGrid(value: str):
    return float(value[:-3])
