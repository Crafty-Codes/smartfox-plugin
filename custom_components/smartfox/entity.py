"""Entity Class of ABB Power-One PVI SunSpec"""

# from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, NAME


class SmartfoxEntity():
    """Representation of an ABB SunSpec Modbus Entity"""
    def __init__(self, config_entry, sensor_data):
        self._entry = config_entry
        self._data = sensor_data
        self._device_model = "smartfox stuff"

    @property
    def unique_id(self) -> str:
        """Return a unique ID to use for this entity"""
        return f"{NAME}_{self._entry.data['host']}"


    @property
    def device_info(self):
        """Return device attributes"""
        return {
            "identifiers": {(NAME, self._entry.data['host'])},
            "name": "name",
            "model": self._device_model,
            "manufacturer": "smartfox",
            "sw_version": "0.0.1",
            "via_device_id": "asasdf",
        }