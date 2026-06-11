# MELCloud Extended

Custom Home Assistant integration based on the official MELCloud integration.

This variant adds Air-to-Water entities for technical water flow control:

- Heating flow temperature setpoint
- Cooling flow temperature setpoint
- Zone operation mode selector

## Installation with HACS

1. Open HACS in Home Assistant.
2. Go to Integrations.
3. Open the three-dot menu and choose Custom repositories.
4. Add this repository URL:

   `https://github.com/VanHelsing2048/MELCloudExtended`

5. Select category `Integration`.
6. Install `MELCloud Extended`.
7. Restart Home Assistant.

The integration domain is still `melcloud`, so this custom component overrides the
built-in Home Assistant MELCloud integration while it is installed.

## Updating

Updates are distributed through Git tags/releases. HACS will detect newer versions
after they are pushed to GitHub.

## Uninstall

Remove the custom integration from HACS and restart Home Assistant. Home Assistant
will fall back to the built-in MELCloud integration.
