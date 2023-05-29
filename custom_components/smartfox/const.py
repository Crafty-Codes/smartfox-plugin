from .data import SmartfoxData
from homeassistant.const import (
    UnitOfPower
)

DOMAIN = "smartfox"
NAME = DOMAIN
CONF_HOST = "host"

DEFAULT_HOST = "http://smartfox/values.xml"

SENSORS = list()

SENSORS.append(SmartfoxData(
        name="To Grid",
        key="toGridValue",
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        change=lambda value : float(value[:-3])
    ))
SENSORS.append(SmartfoxData(
        name="Production",
        key="hidProduction",
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        change=lambda value : float(value[:-3])
    ))

