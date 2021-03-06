# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [VisualBehavior_Task1A_v1.0.2] - 2018-11-21 (BROKEN)

### Changed

- Fix ophys 7a hard crash issue, by pulling MovieStim.py file directly from cam2p_scripts instead of a hard-coded path

### Notes

- The intended fix (Stage 7a) works as intended, however the regimen is broken because the change branched upstream of the 1.0.1 bug fix branch
- Regimen 1.0.3 is targeted to repair the issue

## [VisualBehaviorEPHYS_Task1A_v0.0.5] - 2019-07-16

- change replay script url to public stash url (hopefully doesnt expire?)

## [VisualBehaviorEPHYS_Task1A_v0.0.4] - 2019-07-16 (BROKEN)

- added replay script for EPHYS*1_images*\* stages

## [VisualBehavior_Task1A_v1.0.1] - 2018-10-31

### Changed

- fixes bad stimulus class name

## [VisualBehavior_Task1A_v1.0.0] - 2018-10-22 (BROKEN)

### Added

- Added countdown stimulus to start of each ophys behavior session.
- Added fingerprint stimulus to end of each ophys behavior session.
- Added "omitted flashes" to ophys sessions with 5% omission probability.

### Changed

- Disabled warmup trials on physiology stages and "handoff ready" stage of training.
- Disabled automatic progression between physiology stages.
- Revised naming conventions of stages. Training stages are prefaced with "TRAINING*" and physiology sessions are prefaced with "OPHYS*".
- Modified ophys stimulus sequence to interleave passive sessions between active of the same image set.
- Changed ophys stage names to be all unique (0-7).
- Switched ophys stage B to use image_set_d_parameters instead of image_set_c_parameters.

### Notes

- This regimen fails because the stimulus class value is set to "grating OPHYS_0_images_A_habituation" but should say "grating"
- Regimen 1.0.1 addresses this issue

## [VisualBehavior_Task1A_v0.3.1] - 2018-09-05

### Changed

- Fixed error in file paths for physiology image sets.

## [VisualBehavior_Task1A_v0.3.0] - 2018-08-16

### Changed

- Uses geometric sampling on stages with flashed images or gratings.
- Ends trials relative to end of response window rather than trial start.
- Expand start_stop_padding to 300 seconds.
- Disables `min_no_lick_time`.

## [VisualBehavior_Task1A_v0.2.4] - 2018-08-08

### Added

- Adds habituation stage.

## [VisualBehavior_Task1A_v0.2.3] - 2018-07-26

### Added

- Adds 300ms timeout.

## [VisualBehavior_Task1A_v0.2.2] - 2018-07-09

### Changed

- Fixes misnamed condition to leave "0_gratings_autorewards_15min" stage.

## [VisualBehavior_Task1A_v0.2.1] - 2018-07-09

### Changed

- Fixes image file paths for Windows.

## [VisualBehavior_Task1A_v0.2.0] - 2018-06-11

### Changed

- Major refactor of planned training for production.

[visualbehavior_task1a_v1.0.2]: https://github.com/AllenInstitute/mtrain_regimens/compare/VisualBehavior_Task1A_v1.0.1...VisualBehavior_Task1A_v1.0.2
[visualbehavior_task1a_v1.0.1]: https://github.com/AllenInstitute/mtrain_regimens/compare/VisualBehavior_Task1A_v1.0.0...VisualBehavior_Task1A_v1.0.1
[visualbehavior_task1a_v1.0.0]: https://github.com/AllenInstitute/mtrain_regimens/compare/VisualBehavior_Task1A_v0.3.1...VisualBehavior_Task1A_v1.0.0
[visualbehavior_task1a_v0.3.1]: https://github.com/AllenInstitute/mtrain_regimens/compare/VisualBehavior_Task1A_v0.3.0...VisualBehavior_Task1A_v0.3.1
[visualbehavior_task1a_v0.3.0]: https://github.com/AllenInstitute/mtrain_regimens/compare/VisualBehavior_Task1A_v0.2.4...VisualBehavior_Task1A_v0.3.0
[visualbehavior_task1a_v0.2.4]: https://github.com/AllenInstitute/mtrain_regimens/compare/VisualBehavior_Task1A_v0.2.3...VisualBehavior_Task1A_v0.2.4
[visualbehavior_task1a_v0.2.3]: https://github.com/AllenInstitute/mtrain_regimens/compare/VisualBehavior_Task1A_v0.2.2...VisualBehavior_Task1A_v0.2.3
[visualbehavior_task1a_v0.2.2]: https://github.com/AllenInstitute/mtrain_regimens/compare/VisualBehavior_Task1A_v0.2.1...VisualBehavior_Task1A_v0.2.2
[visualbehavior_task1a_v0.2.1]: https://github.com/AllenInstitute/mtrain_regimens/compare/VisualBehavior_Task1A_v0.2.0...VisualBehavior_Task1A_v0.2.1
[visualbehavior_task1a_v0.2.0]: https://github.com/AllenInstitute/mtrain_regimens/compare/v0.1.3...VisualBehavior_Task1A_v0.2.0
