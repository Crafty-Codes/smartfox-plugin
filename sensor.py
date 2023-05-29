from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .__init__ import HubDataUpdateCoordinator
from .model import SmartfoxEntityDescription
from .entity import SmartfoxEntity
from .api import SmartfoxApi
from .const import (
    DOMAIN,
    SENSOR_TYPES,
    NAME
    )

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_devices):
    hub = hass.data[DOMAIN][entry.entry_id]
    sensors = []

    sensors.append(SmartfoxSensor(hub, entry, SENSOR_TYPES[0]))

    async_add_devices(sensors)

    return True


class SmartfoxSensor(SmartfoxEntity, SensorEntity):
    """Representation of an ABB SunSpec Modbus sensor"""
    def __init__(self, hub: HubDataUpdateCoordinator, config_entry, sensor_data: SmartfoxEntityDescription):
        super().__init__(
            config_entry, sensor_data
        )
        self._hub = hub.api
        self._device_name = NAME
        self._name = sensor_data.name
        self._key = sensor_data.key
        self._unit_of_measurement = sensor_data.native_unit_of_measurement
        self._remove = sensor_data.remove
        # self._icon = sensor_data["icon"]
        # self._device_class = sensor_data.device_class
        # self._state_class = sensor_data.state_class

    async def async_update(self):
        # update the state of the sensor here
        self._state = "asdf"

    @property
    def has_entity_name(self):
        """Return the name"""
        return True

    @property
    def name(self):
        """Return the name"""
        return f"{self._name}"

    @property
    def native_unit_of_measurement(self):
        """Return the unit of measurement"""
        return self._unit_of_measurement

    # @property
    # def icon(self):
    #     """Return the sensor icon."""
    #     return self._icon

    # @property
    # def device_class(self):
    #     """Return the sensor device_class."""
    #     return self._device_class

    # @property
    # def state_class(self):
    #     """Return the sensor state_class."""
    #     return self._state_class

    @property
    def native_value(self):
        """Return the state of the sensor."""
        print("asdfasdfasdfasdfasdf")
        if self._key in self._hub.data:
            if self._remove:
                return self._remove(self._hub.data[self._key])
            return self._hub.data[self._key]
    
    # @property
    # def state_attributes(self) -> Optional[Dict[str, Any]]:
    #     """Return the attributes"""
    #     return None

    @property
    def should_poll(self) -> bool:
        """Data is delivered by the hub"""
        return False