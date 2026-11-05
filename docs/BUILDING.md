# Build the current Customizer

The Lua package needs the matching native menu changes. Copying it into an
unmodified Chronicle executable will not provide this fork's numeric input,
character folders or weapon-tree integration.

This repository distributes the Customizer package plus a native source patch,
not an unrelated replacement for the framework repository's Git history.
The patch is based on Chronicle Mod Framework commit
`17b20f181db2106f65d03809adc5fcc12b050cf3`.
The exact repository, commit and patch are recorded in
[`framework/base.json`](../framework/base.json).

## Prepare the source

Run from a fresh clone of this Chronicle-Customizer repository:

```powershell
git clone --recurse-submodules https://github.com/anxiousintrovert/Chronicle-Mod-Framework.git build/framework
git -C build/framework checkout --detach 17b20f181db2106f65d03809adc5fcc12b050cf3
git -C build/framework submodule update --init --recursive
$patch = (Resolve-Path framework/chronicle-customizer.patch).Path
git -C build/framework apply --check $patch
git -C build/framework apply $patch
```

Use a clean checkout. If the check fails, stop and inspect the base revision and
local changes rather than forcing the patch or overwriting a working installation.
The upstream repository name is a build dependency; this Customizer project is
owned and published at `depressionkiller2003/Chronicle-Customizer`.

## Compile and install

Follow `build/framework/docs/WINDOWS.md` for dependencies, Clang setup and Windows
build requirements. From `build/framework`, build with:

```powershell
.\build.bat windows-x64-release
```

From this Customizer repository, install the mod beside the newly built executable:

```powershell
New-Item -ItemType Directory -Force build/framework/port/build/windows-x64-release/mods | Out-Null
Copy-Item -Recurse mods/chronicle.customizer build/framework/port/build/windows-x64-release/mods/
```

Install into a fresh destination; do not overwrite another mod or existing copy
without a backup. Provide your own supported Dark Cloud game data, then launch
the executable. Enable Chronicle Customizer in the Mod Manager and restart.

The patch includes the deterministic weapon-tree links, normal-menu button and
name display, numeric action handling, ordered/locked character folders, source
package and regression checks. Native implementation stays under `port/`, apart
from two small `PORT`-guarded calls into the existing weapon input loop; PS2 builds
omit those calls.

No personal saves, disc images, extracted game data or prebuilt executable are
included. Existing GitHub release downloads are separate from this source update.
