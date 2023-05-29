import xml.etree.ElementTree as ET
import requests
from homeassistant.core import HomeAssistant


class SmartfoxApi:
    def __init__(self, host: str, hass: HomeAssistant):
        self._host = host
        self._hass = hass
        self.data = {}


    async def async_getData(self) -> str | None:
        try:
            response = await self._hass.async_add_executor_job(requests.get, self._host)
            xml = ET.fromstring(response.text)

            for value in xml:
                valueId = value.attrib["id"]
                data[valueId] = value.text

        except Exception as e:
            return None