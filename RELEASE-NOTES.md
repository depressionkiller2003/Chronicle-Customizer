# Chronicle Customizer v0.2.0 — Windows x64

This release updates the downloadable Windows build to match current Customizer
development. It supersedes v0.1.1; previous releases remain available as history.

## Included features

- Custom Gilda numeric entry with the existing additive behavior.
- Maximum HP and base DEF editing for all six characters.
- Ordered folders: Toan, Xiao, Goro, Ruby, Ungaga, Osmond; HP then DEF.
- Story-based locks for characters who have not joined the party.
- Light-orange **View Build-up Tree** at the bottom of the normal weapon action
  menu, including when optional actions such as Status Break are available.
- Named normal build-up destinations instead of “???”, without bypassing requirements.
- Read-only future weapon paths, branches, terminal weapons and Mardan routes.

## Download and start

Download **Chronicle-Customizer-v0.2.0-windows-x64.zip**, extract it into a new
folder, and open `darkcloud.exe` or `Launch-Chronicle-Customizer.bat`.
Read `START-HERE.txt`. Supply your own supported Dark Cloud data; no game data
or disc image is included. Enable Chronicle Customizer in the Mod Manager and
restart if this is your first installation.

The ZIP includes the current executable, data extraction tool, runtime DLLs,
UI fonts/translations/glyphs, mod source, credits/notices and build/checksum data.
It excludes personal saves, config/profile files, local backups and extracted
game assets. The graphics driver/Vulkan runtime comes from your PC.

## Compatibility and saves

Application release: **v0.2.0**. The mod's saved identity remains
**`chronicle.customizer` version `1.0.0`**. No save migration is run by this update.
Back up saves and use a spare slot for testing. Normal gameplay may autosave.
Older saves requiring `liam.custom-stats` are not automatically converted.

## Validation and limits

Windows Release build, package validation, Lua callbacks, numeric/recruitment
checks and tree/action-order tests passed locally. Isolated scripted gameplay
verified terminal/branching trees, the native button, controller Back and named
upgrade choices. The packaged executable is checked after ZIP extraction with a
separate test save root. Broader other-character, mouse, recruitment and
save/reload gameplay remains manual; Linux/macOS gameplay is not validated.

This is a development project; the status above does not imply exhaustive testing.
Source and build instructions are in the repository. SHA256 checksums accompany
the ZIP, and `BUILD-INFO.json` identifies its matching source revision.
