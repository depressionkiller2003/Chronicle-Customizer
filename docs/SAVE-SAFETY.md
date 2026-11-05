# Saves and compatibility

- Back up your saves before experimenting, and use a spare slot for testing.
- Loading a save or viewing a tree does not require manually saving.
- Save HP, DEF or Gilda edits only if you want to retain them. Normal gameplay
  may autosave, so an existing backup remains important.
- Keep the exact required mod available for saves that depend on it.

The package ID remains **`chronicle.customizer`**, version **`1.0.0`**. Do not
rename it or reinstall the retired `liam.custom-stats` package alongside it.
Older saves that require that retired ID are not automatically migrated by this
source package. Do not manually rewrite save trailers or checksums without a
separate, verified migration procedure and original backups.

The tree preview is read-only. The native write API rejects character edits for
party members who have not joined. Revealing a build-up destination's name does
not bypass its requirements.

Development gameplay checks used an isolated executable and separate test save
root. Personal saves, local migration utilities, backups, extracted assets and
disc images are not included in this repository update.
