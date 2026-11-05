# Use Chronicle Customizer

Use a compatible executable built with the
[native patch](BUILDING.md), and install `mods/chronicle.customizer` beside it.
Enable the package under **Options → Mods → Mod Manager**, then restart.
Keep one installed copy with ID `chronicle.customizer`.

## Character editing

Load a save, select Chronicle Customizer in the Mod Manager and open **R1 Actions**.
The top level contains Custom Gilda followed by **Toan, Xiao, Goro, Ruby, Ungaga,
Osmond**, in that order. Each joined character's folder contains HP then DEF.
Unrecruited characters display **(Locked)** and their folders cannot be opened.

| Action | Range | What it does |
| --- | --- | --- |
| HP | 1–32767 | Sets maximum HP; lowering it clamps current HP, increasing it does not heal |
| DEF | 0–32767 | Sets that character's base defense |
| Custom Gilda | 1–65535 | Adds the entered amount to the existing balance |

Select an action, type digits and press Enter. Backspace edits; Escape cancels
entry. Close the menus and allow gameplay to tick before checking the stats.
The pane displays readiness and the last action result. Back returns from a
character folder to that character's row.

For Gilda, keep the current balance plus the entered amount at or below 65535.
The mod retains the existing additive behavior rather than replacing the wallet.

Story locks use the loaded save's joined-party count. They update when another
save is loaded or a character joins. Numeric submission rechecks recruitment,
and the native API also rejects edits to characters who have not joined.

## Weapon build-up tree

Open the normal **Weapon** menu, choose a weapon and open its action list.
The light-orange **View Build-up Tree** is below all available normal actions,
including Upgrade, Status Break/Synthesize and Build-Up. It is not a duplicate
weapon inventory in the Customizer stat menu.

- Up/Down selects a tree row.
- Left/Right pages through its details; Cross/Details advances details too.
- Circle/Back returns to the selected weapon's normal action menu.
- Mouse users can select rows and use Details and Back.

The preview shows future native paths, forks, terminal weapons and special Mardan
routes. Long names may be shortened in the left list; selecting a row shows its
full name and path on the right. No external build-up chart is required.

The normal Build-Up destination menu now reveals weapon names even before their
requirements are met. The game's actual requirements still apply. Previewing
does not equip, alter, build up or status-break weapons. These native additions
are enabled while the Customizer package is active.

See [save safety](SAVE-SAFETY.md) and [validation status](TESTING.md).
