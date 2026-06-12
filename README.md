# MELCloud Extended

MELCloud Extended is a Home Assistant custom integration based on the official
MELCloud integration.

It keeps the same integration domain, `melcloud`, and adds extra Air-to-Water
controls that are available in MELCloud but are not exposed by the official Home
Assistant integration.

## Origin and attribution

This repository is a derivative custom integration based on the official
Home Assistant Core MELCloud integration.

Original source:

`https://github.com/home-assistant/core/tree/dev/homeassistant/components/melcloud`

The original Home Assistant integration lists `@erwindouna` as code owner. This
repository is maintained separately by `@VanHelsing2048` and adds extra
Air-to-Water entities on top of that original implementation.

Home Assistant Core is licensed under the Apache License 2.0. A copy of that
license is included in [LICENSE.md](LICENSE.md).

## Added entities

For Air-to-Water devices, this custom integration adds:

- Heating flow temperature setpoint
- Cooling flow temperature setpoint
- Zone operation mode selector

The zone operation mode selector can expose modes supported by the device, such as:

- `heat-thermostat`
- `heat-flow`
- `curve`
- `cool-thermostat`
- `cool-flow`

## Important compatibility note

This custom integration uses the same domain as the built-in Home Assistant
integration:

`melcloud`

When installed under `/config/custom_components/melcloud`, Home Assistant loads
this custom version instead of the built-in MELCloud integration. Your existing
MELCloud config entry should remain in place.

To go back to the official Home Assistant integration, remove this custom
integration and restart Home Assistant.

## Installation with HACS

1. Open HACS in Home Assistant.
2. Go to `Integrations`.
3. Open the three-dot menu.
4. Select `Custom repositories`.
5. Add this repository URL:

   `https://github.com/VanHelsing2048/MELCloudExtended`

6. Select category `Integration`.
7. Install `MELCloud Extended`.
8. Restart Home Assistant.

After the restart, check the MELCloud device page. The new `number` and `select`
entities should appear on supported Air-to-Water devices.

## Updates

Versions are published with Git tags, for example `v0.1.1`.

HACS can detect new tagged versions and offer updates from its normal update
flow.

See [CHANGELOG.md](CHANGELOG.md) for version notes.

## Security

This repository does not require storing MELCloud credentials in files.

Authentication remains handled by Home Assistant's existing MELCloud config
entry and the `python-melcloud` library declared in the integration manifest.

Before installing any custom integration, review the code and make sure the
repository URL is the one you expect:

`https://github.com/VanHelsing2048/MELCloudExtended`

Do not commit logs, Home Assistant storage files, access tokens, cookies, or
MELCloud credentials to this repository.

## Rollback

If Home Assistant fails to start, or the integration behaves unexpectedly:

1. Remove the custom integration from HACS, or delete:

   `/config/custom_components/melcloud`

2. Restart Home Assistant.
3. Home Assistant will fall back to the built-in MELCloud integration.

Your MELCloud config entry should not need to be recreated.

## Current limitations

This integration has been statically validated and checked against the
`python-melcloud==0.1.3` API used by Home Assistant.

Runtime behavior still depends on the specific MELCloud device model, supported
Air-to-Water modes, and the data returned by the MELCloud cloud API.
