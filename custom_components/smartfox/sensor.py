from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import Entity
import asyncio
from .const import (
    DOMAIN,
    NAME,
    SENSORS,
    CONF_HOST
)

from .data import SmartfoxData
from .api import SmartfoxApi

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_devices):
    sensors = []

    api = SmartfoxApi(entry.data[CONF_HOST], hass)

    for i in range(len(SENSORS)):
        sensors.append(SmartfoxSensor(api, entry, SENSORS[i]))

    async_add_devices(sensors)

    return True


class SmartfoxSensor(Entity):
    """Representation of a Smartfox sensor."""
    def __init__(self, api : SmartfoxApi, config_entry, sensor_data : SmartfoxData):
        super().__init__()
        self._hub = api
        self._device_name = NAME
        self._name = sensor_data.name
        self._key = sensor_data.key
        self._unit_of_measurement = sensor_data.native_unit_of_measurement
        self._change = sensor_data.change
        self._available = True#

    @property
    def name(self) -> str:
        """Return the name of the entity."""
        return self._name

    @property
    def unique_id(self) -> str:
        """Return the unique ID of the sensor."""
        return f"{self._device_name}_{self._name}"

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self._available

    @property
    def state(self) -> str | None:
        if self._key in self._hub.data:
            if self._remove:
                return self._remove(self._hub.data[self._key])
            return self._hub.data[self._key]

    @property
    def native_unit_of_measurement(self):
        """Return the unit of measurement"""
        return self._unit_of_measurement

    @property
    def native_value(self):
        """Return the state of the sensor."""
        print("asdfasdfasdfasdfasdf")
        if self._key in self._hub.data:
            if self._remove:
                return self._remove(self._hub.data[self._key])
            return self._hub.data[self._key]

    async def async_update(self) -> None:
        """Update all sensors."""
        try:
            print("Now update")
            await self._hub.async_getData()
        except Exception as e:
            pass
