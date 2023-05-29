"""The smartfox_reader integration."""
from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from datetime import timedelta
from .api import SmartfoxApi
from .const import DOMAIN, CONF_HOST

import logging
_LOGGER: logging.Logger = logging.getLogger(__package__)
# TODO List the platforms that you want to support.
# For your initial PR, limit it to 1 platform.
# PLATFORM: list[Platform] = [Platform.SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up smartfox_reader from a config entry."""

    hass.data.setdefault(DOMAIN, {})

    try:
        api = SmartfoxApi(entry.data[CONF_HOST])
        coordinator = HubDataUpdateCoordinator(hass, api, entry)
        await coordinator.async_config_entry_first_refresh()
    except ConnectionException as connerr:
        raise ConfigEntryNotReady(f"Problem connecting to device {entry.data[CONF_HOST]}")

    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setup(entry, Platform.SENSOR)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload(entry.entry_id):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


class HubDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from the API."""

    def __init__(
        self,
        hass: HomeAssistant,
        hub: SmartfoxApi,
        entry: ConfigEntry
    ) -> None:
        """Initialize."""
        self.api = hub
        self.hass = hass
        self.entry = entry

        # self.platforms = []
        scan_interval = timedelta(seconds=2)

        # self.unsub = entry.add_update_listener(async_reload_entry)
        _LOGGER.debug(
            "Setup entry with scan interval %s. Host: %s Port: %s ID: %s",
            scan_interval,
            entry.data.get(CONF_HOST)
        )
        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=scan_interval)

    async def _async_update_data(self):
        """Update data via library."""
        try:
            print("hello update")
            return await self.api.async_getData()
        except Exception as exception:
            raise UpdateFailed() from exception
