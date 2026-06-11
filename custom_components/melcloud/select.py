"""Support for MELCloud select entities."""

from pymelcloud import DEVICE_TYPE_ATW
from pymelcloud.atw_device import Zone

from homeassistant.components.select import SelectEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .coordinator import MelCloudConfigEntry, MelCloudDeviceUpdateCoordinator
from .entity import MelCloudEntity


async def async_setup_entry(
    _hass: HomeAssistant,
    entry: MelCloudConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up MELCloud select entities based on config_entry."""
    coordinators = entry.runtime_data

    entities = [
        AtwZoneOperationModeSelect(coordinator, zone)
        for coordinator in coordinators.get(DEVICE_TYPE_ATW, [])
        for zone in coordinator.device.zones
        if zone.operation_modes
    ]
    async_add_entities(entities)


class AtwZoneOperationModeSelect(MelCloudEntity, SelectEntity):
    """Representation of an ATW zone operation mode select entity."""

    _attr_translation_key = "zone_operation_mode"

    def __init__(
        self,
        coordinator: MelCloudDeviceUpdateCoordinator,
        zone: Zone,
    ) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._zone = zone

        self._attr_unique_id = (
            f"{coordinator.device.serial}-{zone.zone_index}-operation-mode"
        )
        self._attr_device_info = coordinator.zone_device_info(zone)

    @property
    def current_option(self) -> str | None:
        """Return the selected operation mode."""
        return self._zone.operation_mode

    @property
    def options(self) -> list[str]:
        """Return available operation modes."""
        return self._zone.operation_modes

    async def async_select_option(self, option: str) -> None:
        """Set operation mode."""
        await self._zone.set_operation_mode(option)
        await self.coordinator.async_request_refresh()
