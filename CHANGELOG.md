# Changelog

All notable changes to MELCloud Extended are documented in this file.

## 0.1.4 - 2026-06-12

### Documentation

- Added origin and attribution notes for the official Home Assistant Core
  MELCloud integration.
- Added Apache License 2.0 license file copied from Home Assistant Core.

## 0.1.3 - 2026-06-12

### Changed

- Updated integration code owner to `@VanHelsing2048`.
- Updated integration documentation URL to this repository.

## 0.1.2 - 2026-06-12

### Documentation

- Added this changelog.
- Improved repository documentation for HACS installation, rollback, update flow,
  and security expectations.

### Security

- Documented that MELCloud credentials must not be stored in repository files.
- Documented that authentication remains managed by Home Assistant and the
  `python-melcloud` dependency.

## 0.1.1 - 2026-06-12

### Fixed

- Fixed invalid Python exception syntax in the config flow.
- Validated Python syntax for all integration files.
- Validated JSON metadata files.

## 0.1.0 - 2026-06-11

### Added

- Initial HACS-compatible repository structure.
- Custom MELCloud integration under `custom_components/melcloud`.
- Air-to-Water heating flow temperature number entity.
- Air-to-Water cooling flow temperature number entity.
- Air-to-Water zone operation mode select entity.
- HACS metadata.
