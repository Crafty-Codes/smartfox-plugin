from dataclasses import dataclass

from homeassistant.components.sensor import SensorEntityDescription

@dataclass
class SmartfoxEntityDescriptionMixin:
    remove: None

@dataclass
class SmartfoxEntityDescription(SensorEntityDescription, SmartfoxEntityDescriptionMixin):
    """Sensor entity description for smartfox"""
