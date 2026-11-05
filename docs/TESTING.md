# Current validation

Status: 5 November 2026. These checks describe development evidence, not a claim
that every character, weapon, platform and gameplay scenario has been tested.

## Passed locally

- Windows x64 Release game build with the native patch.
- All 13 Lua registrations, six character IDs, integer HP/DEF calls, bounds and
  Gilda reward chunking.
- Numeric lookup and recruitment rules across party sizes 0–6.
- Tree forks, merged paths, terminal nodes and cycle/depth/size limits.
- All optional native weapon action-row combinations: the tree action is last,
  including when Status Break is available.
- Fifteen framework author-tool/source-integrity Python tests.
- Isolated scripted gameplay: tree button and cursor, Dagger's terminal tree,
  Crysknife's branching tree, controller Back, and named Small Sword/Sand Breaker
  choices in the normal build-up menu.
- Read-only CRC32 and mod ID checks of the local migrated saves.

The user confirmed the ordered character folder UI and tree opening in normal
gameplay. The native menu's Status Break-ready layout was checked through all
action combinations; a normal-play check with such a weapon remains useful.

## Remaining gameplay coverage

- Other characters' weapon paths and special routes.
- Mouse controls and each player's actual controller/keyboard bindings.
- Story recruitment transitions and early/late save changes.
- Broader stat save/reload and normal build-up/status-break gameplay.
- Linux/macOS gameplay with these additions.

The complete framework/game test suite is not claimed as passed by these targeted
checks. The asset-free [source-check workflow](../.github/workflows/source-checks.yml)
validates the native patch against the pinned base, package format, helper rules
and actual Lua callbacks. It does not test rendered gameplay.
