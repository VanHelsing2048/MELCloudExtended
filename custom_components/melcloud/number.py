"""Support for MELCloud number entities."""

from collections.abc import Callable
import dataclasses
from typing import Any

from pymelcloud import DEVICE_TYPE_ATW
from pymelcloud.atw_device import Zone

from homeassistant.components.number import (
    NumberDeviceClass,
    NumberEntity,
    NumberEntityDescription,
)
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .coordinator import MelCloudConfigEntry, MelCloudDeviceUpdateCoordinator
from .entity import MelCloudEntity


@dataclasses.dataclass(frozen=True, kw_only=True)
class MelCloudNumberEntityDescription(NumberEntityDescription):
    """Describes MELCloud number entity."""

    value_fn: Callable[[Zone], float | None]
    set_fn: Callable[[MelCloudDeviceUpdateCoordinator, Zone, float], Any]
    enabled: Callable[[Zone], bool]


async def _set_heat_flow_temperature(
    coordinator: MelCloudDeviceUpdateCoordinator, zone: Zone, value: float
) -> None:
    """Set heating flow temperature for a zone."""
    await zone.set_target_heat_flow_temperature(value)
    await coordinator.async_request_refresh()


async def _set_cool_flow_temperature(
    coordinator: MelCloudDeviceUpdateCoordinator, zone: Zone, value: float
) -> None:
    """Set cooling flow temperature for a zone."""
    await zone.set_target_cool_flow_temperature(value)
    await coordinator.async_request_refresh()


ATW_ZONE_NUMBERS: tuple[MelCloudNumberEntityDescription, ...] = (
    MelCloudNumberEntityDescription(
        key="heat_flow_temperature",
        translation_key="heat_flow_temperature",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=NumberDeviceClass.TEMPERATURE,
        native_min_value=5,
        native_max_value=60,
        native_step=0.5,
        value_fn=lambda zone: zone.target_heat_flow_temperature,
        set_fn=_set_heat_flow_temperature,
        enabled=lambda zone: zone.target_heat_flow_temperature is not None,
    ),
    MelCloudNumberEntityDescription(
        key="cool_flow_temperature",
        translation_key="cool_flow_temperature",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=NumberDeviceClass.TEMPERATURE,
        native_min_value=5,
        native_max_value=60,
        native_step=0.5,
        value_fn=lambda zone: zone.target_cool_flow_temperature,
        set_fn=_set_cool_flow_temperature,
        enabled=lambda zone: zone.target_cool_flow_temperature is not None,
    ),
)


async def async_setup_entry(
    _hass: HomeAssistant,
    entry: MelCloudConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up MELCloud number entities based on config_entry."""
    coordinators = entry.runtime_data

    entities = [
        AtwZoneNumber(coordinator, zone, description)
        for coordinator in coordinators.get(DEVICE_TYPE_ATW, [])
        for zone in coordinator.device.zones
        for description in ATW_ZONE_NUMBERS
        if description.enabled(zone)
    ]
    async_add_entities(entities)


class AtwZoneNumber(MelCloudEntity, NumberEntity):
    """Representation of an ATW zone number entity."""

    entity_description: MelCloudNumberEntityDescription

    def __init__(
        self,
        coordinator: MelCloudDeviceUpdateCoordinator,
        zone: Zone,
        description: MelCloudNumberEntityDescription,
    ) -> None:
        """Initialize the number entity."""
        super().__init__(coordinator)
        self._zone = zone

        if zone.zone_index != 1:
            description = dataclasses.replace(
                description,
                key=f"{description.key}-zone-{zone.zone_index}",
            )
        self.entity_description = description

        self._attr_unique_id = (
            f"{coordinator.device.serial}-{zone.zone_index}-{description.key}"
        )
        self._attr_device_info = coordinator.zone_device_info(zone)

    @property
    def native_value(self) -> float | None:
        """Return the current number value."""
        return self.entity_description.value_fn(self._zone)

    async def async_set_native_value(self, value: float) -> None:
        """Set the number value."""
        await self.entity_description.set_fn(self.coordinator, self._zone, value)
