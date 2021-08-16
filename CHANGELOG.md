# Changelog

All notable changes to this project will be documented in this file.
We follow the [Semantic Versioning 2.0.0](http://semver.org/) format.

## 1.0.0 - 2021-08-16

We have been using 0.9.0 for nine months. This release contains a few fixes and tweaks that improves the experience for us at SVT. We have found that the noop-event was much more common and the channel was overflown with noop-messages making it harder for us that use the bot to see whats going on. This release wraps up these experiences with a 1.0 release.

### Changed

- Rework the room creation logic, the `group_size` is the desired room size.
  This is not a hard limit, for example with `group_size` set to `3`, and 4 people, there will be a single room generated with four people inside. Splitting will occur if there is six people or more.
- Rooms will be generated if there are two people or more (was three).

### Removed

- The "noop"-message has been removed to make the channel less noisy.

## 0.9.0 - 2020-11-27

### Added

- Import the existing project files from the internal repository at SVT.
  To make it more generic and useful for others. The source code has been
  refactored to a package. I will promote this release to 1.0.0 when we have moved over using this package our self.

### Deprecated

- Nothing.

### Removed

- Nothing.

### Fixed

- Nothing.
