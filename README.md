# Chronicle Customizer

**An in-game customisation mod for the Chronicle Windows PC port of Dark Cloud 1.**

Chronicle Customizer gives players control over character stats and Gilda through
the in-game Mod Manager, and adds named weapon upgrade choices plus a build-up
tree preview to the normal Weapon menu.

**Current progress: 5 November 2026.** Mod ID: `chronicle.customizer`. Version:
`1.0.0`, retained for compatible existing saves. This remains a work in progress.

## Implemented

| Feature | Current behavior |
| --- | --- |
| Custom Gilda | Enter an amount to add to the existing balance |
| Six-character HP/DEF | Maximum HP and base defense for Toan, Xiao, Goro, Ruby, Ungaga and Osmond |
| Ordered character folders | Toan → Xiao → Goro → Ruby → Ungaga → Osmond; each contains HP then DEF |
| Story locks | Characters who have not joined show **(Locked)** and cannot be edited |
| Native weapon tree | Light-orange **View Build-up Tree** at the bottom of the normal weapon action list |
| Optional action layout | The tree button stays below actions such as Status Break and Build-Up |
| Named build-up choices | Destination names appear instead of “???” even before requirements are met |
| Read-only paths | Browse future native weapon branches without changing a weapon |

There are still 13 underlying stat/currency actions, grouped into Custom Gilda
and six character folders. There is no duplicate weapon inventory in that menu.

- **HP:** 1–32767. Sets maximum HP; raising capacity does not heal.
- **DEF:** 0–32767. Sets character base defense.
- **Custom Gilda:** 1–65535 added to your wallet. Keep the resulting balance at
  or below **65,535**; this adds rather than replaces your balance.

## Where to find everything

**Stats:** Options → Mods → Mod Manager → Chronicle Customizer → R1 Actions.
Select HP/DEF, type a number and press Enter. Close the menus and resume gameplay
briefly so the action can run. Unrecruited character folders remain locked.

**Weapon trees:** Weapon → select a weapon → action list → **View Build-up Tree**.
Up/Down selects a branch, Left/Right reads its details, and Circle/Back returns to
that weapon. The normal Build-Up menu also displays named destinations. Actual
build-up requirements are still enforced.

Read the [full usage guide](docs/USAGE.md), [save guidance](docs/SAVE-SAFETY.md),
and [validation status](docs/TESTING.md).

## Source and installation

This update publishes the current source and documentation:

- [`mods/chronicle.customizer`](mods/chronicle.customizer): installable Lua package.
- [`framework/chronicle-customizer.patch`](framework/chronicle-customizer.patch):
  matching native host changes and regression checks.
- [`framework/base.json`](framework/base.json): exact framework base revision.
- [Build instructions](docs/BUILDING.md) and [development changelog](CHANGELOG.md).

The Lua package needs an executable built with the matching native changes. It
is not a drop-in replacement for an unmodified upstream Chronicle host. Enable
it in the Mod Manager and restart after installation.

[GitHub Releases](https://github.com/depressionkiller2003/Chronicle-Customizer/releases)
contains separately published downloads. Existing v0.1.0-beta/v0.1.1 downloads
may predate the source features described here; this source update does not
replace those release assets or claim a new ready-to-play binary release.

No disc images, extracted game data, personal saves, local recovery copies or
prebuilt executable are included in this source update. Supply your own supported
Dark Cloud game data.

## Validation and remaining work

The Windows x64 Release build and targeted Lua/C++ regression checks passed
locally. Isolated scripted game tests verified the button, terminal and branching
trees, controller Back and named upgrade choices. The user confirmed character
folders and tree opening in normal play. The asset-free workflow checks source,
package callbacks and traversal rules; it does not establish gameplay coverage.

Other characters' weapon routes, mouse controls, recruitment transitions and
broader save/reload checks remain manual. Linux/macOS gameplay with these
additions has not been validated. See [testing](docs/TESTING.md) for precise scope.

Planned customisation work still includes weapon Attack, Durability, Speed,
Magic, elemental attributes and further gameplay options. Those editors are
**not implemented** by the tree preview.

## Save safety

Back up your saves and use a spare slot for experiments. Loading a save or viewing
the tree does not require saving. Save stat/Gilda edits only when you want to keep
them, remembering that gameplay may autosave. Keep the mod ID/version available
for saves that require it; this package does not automatically migrate older IDs.

## Credits

- **Chronicle developers and contributors** — the original Dark Cloud PC port.
- **Chronicle Mod Framework contributors** — the framework this mod builds on.
- **Dark Cloud community** — feedback, testing and suggestions.

Framework dependency: [Chronicle Mod Framework](https://github.com/anxiousintrovert/Chronicle-Mod-Framework),
which preserves work from [TheMoonPeople/Chronicle](https://github.com/TheMoonPeople/Chronicle).

**Chronicle Customizer — Work in Progress.**
