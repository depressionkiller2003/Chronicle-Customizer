# Development changelog

## v0.2.0 — 5 November 2026

- Updated Windows x64 download to the current built executable and mod.
- Packaged runtime DLLs, UI resources, instructions, credits/notices, source
  revision metadata, an internal file hash manifest and an external ZIP checksum.
- Created an allowlist-based packaging script to exclude developer backups,
  save/config/profile files, extracted game data and disc images.
- Updated README download links and release instructions; previous releases and
  tags remain available. Mod save identity stays `chronicle.customizer` `1.0.0`.

### Features included in v0.2.0

- Added HP and DEF editing for all six characters, using integer Lua arguments.
- Grouped the 13 actions into Custom Gilda and ordered character folders:
  Toan, Xiao, Goro, Ruby, Ungaga, Osmond; HP then DEF inside each.
- Added story-based locked folders, submission-time recruitment checks and
  native rejection of edits for characters who have not joined.
- Preserved Custom Gilda's additive chunked behavior and save-compatible package
  identity `chronicle.customizer` version `1.0.0`.
- Added the light-orange View Build-up Tree button below normal weapon actions,
  including optional Status Break; cursor and mouse rows account for these actions.
- Revealed normal build-up destination names without bypassing requirements.
- Added read-only native tree paths, forks, terminal weapons, special Mardan routes,
  bounded traversal, detail paging and return to the selected weapon action list.
- Included a source patch against a pinned framework revision, including the local
  first-run core-data checks and protection against overwriting a partial extraction.
- Updated project README, package README, usage/build/save/test guides and asset-free
  source regression workflow.

Windows Release and targeted checks passed locally; isolated game tests covered
branching/terminal trees, the button, controller Back and named build-up choices.
Other character paths, mouse input, recruitment transitions and broader gameplay
remain manual. See [validation details](docs/TESTING.md).

The v0.2.0 binary release supersedes earlier downloads without deleting them.
It does not run a save migration or include saves, extracted game data or backups.
The source checkout remains separate from the downloadable Windows executable.
