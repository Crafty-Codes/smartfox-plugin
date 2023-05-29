import xml.etree.ElementTree as ET
import requests

class SmartfoxApi:
    def __init__(self, host: str):
        self._host = host
        self.data = {}


    async def async_getData(self) -> str | None:
        try:
            response = requests.get(self._host)
            xml = ET.fromstring(response.text)

            for value in xml:
                valueId = value.attrib["id"]
                data[valueId] = value.text

        except Exception as e:
            return None