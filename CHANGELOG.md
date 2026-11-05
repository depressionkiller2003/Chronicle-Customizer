# Development changelog

## 5 November 2026 — Current Customizer progress

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

This source update preserves the existing repository history and release tags.
It does not replace earlier GitHub release downloads, run a save migration or
include saves, game data, backups, an executable or a new binary release.
