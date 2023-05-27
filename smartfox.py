import xml.etree.ElementTree as ET
import requests

class smartfox:
    
    def __init__(self, host):
        self.host = host
    
    def get_data(self):
        try:    
            response = requests.get(self.host)

            xml = ET.fromstring(response.text)

            for value in xml:
                print(value.attrib["id"], value.text)

        except Exception as e:
            print(e)

s = smartfox("http://192.168.178.100/values.xml")

s.get_data()
