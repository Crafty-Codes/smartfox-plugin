"""Constants for the smartfox_reader integration."""
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import (
    EntityCategory,
    UnitOfEnergy,
    UnitOfPower,
    UnitOfTemperature,
)

from .model import SmartfoxEntityDescription

DOMAIN = "smartfox"
NAME= "smarfox"
CONF_HOST = "host"


def remover(value: str):
    return float(value[:-3])

SENSOR_TYPES = [
    SmartfoxEntityDescription(
        key="toGridValue",
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        state_class=SensorStateClass.MEASUREMENT,
        name="Power to Grid",
        remove=remover
    ),
]
