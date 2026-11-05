"""Create a Windows release from an explicit allowlist, never a developer-folder ZIP."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import zipfile


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--framework', type=Path, required=True)
    parser.add_argument('--build', type=Path, required=True)
    parser.add_argument('--dependencies', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    version = (repo / 'VERSION').read_text(encoding='utf-8-sig').strip()
    name = f'Chronicle-Customizer-{version}-windows-x64'
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    stage = output / name
    stage.mkdir(exist_ok=False)  # Avoid mixing an older package into a new release.

    def copy(source, destination):
        target = stage / destination
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)

    binaries = ['darkcloud.exe', 'dcdata.exe', 'SDL3.dll', 'libc++.dll',
                'libunwind.dll', 'libwinpthread-1.dll']
    for name in binaries:
        copy(args.build / name, name)
    for source in sorted((args.build / 'lang').iterdir()):
        if source.is_file() and source.suffix in {'.ttf', '.json'}:
            copy(source, 'lang/' + source.name)
    glyphs = args.build / 'glyphs'
    copy(glyphs / 'glyphs.json', 'glyphs/glyphs.json')
    index = json.loads((glyphs / 'glyphs.json').read_text(encoding='utf-8-sig'))
    for atlas in sorted({style['atlas'] for style in index['styles'].values()}):
        if Path(atlas).name != atlas:
            raise ValueError('Unexpected glyph atlas path')
        copy(glyphs / atlas, 'glyphs/' + atlas)
    for name in ['main.lua', 'mod.json']:
        copy(repo / 'mods/chronicle.customizer' / name, 'mods/chronicle.customizer/' + name)
    copy(repo / 'packaging/WINDOWS-README.txt', 'START-HERE.txt')
    copy(repo / 'RELEASE-NOTES.md', 'RELEASE-NOTES.md')
    copy(args.framework / 'CREDITS', 'CREDITS.txt')
    copy(args.framework / 'tools/font/README.md', 'licenses/Community-fonts.md')
    copy(args.framework / 'docs/GLYPHS.md', 'licenses/Controller-glyphs.md')
    copy(args.framework / 'tools/kazarov/LICENSE', 'licenses/Kazarov-MIT.txt')
    copy(args.framework / 'port/third_party/lua/LUA-LICENSE.txt', 'licenses/Lua-MIT.txt')
    copy(args.build / '_deps/nlohmann_json-src/LICENSE.MIT', 'licenses/nlohmann-json-MIT.txt')
    llvm = args.dependencies / 'llvm/llvm-mingw-20260922-ucrt-x86_64'
    copy(llvm / 'LICENSE.TXT', 'licenses/LLVM.txt')
    for name in ['COPYING.MinGW-w64.txt', 'COPYING.MinGW-w64-runtime.txt', 'COPYING.winpthreads.txt']:
        copy(llvm / 'x86_64-w64-mingw32/share/mingw32' / name, 'licenses/' + name)
    copy(args.dependencies / 'sdl/SDL3-3.4.18/LICENSE.txt', 'licenses/SDL3.txt')
    (stage / 'Launch-Chronicle-Customizer.bat').write_text(
        '@echo off\ncd /d "%~dp0"\nstart "" "%~dp0darkcloud.exe"\n', encoding='ascii')

    commit = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip()
    manifest = json.loads((stage / 'mods/chronicle.customizer/mod.json').read_text(encoding='utf-8-sig'))
    info = {'release': version, 'platform': 'windows-x64',
            'repository': 'https://github.com/depressionkiller2003/Chronicle-Customizer',
            'source_commit': commit, 'mod_id': manifest['id'], 'mod_version': manifest['version'],
            'executable_sha256': digest(stage / 'darkcloud.exe'),
            'framework_base': json.loads((repo / 'framework/base.json').read_text(encoding='utf-8'))}
    (stage / 'BUILD-INFO.json').write_text(json.dumps(info, indent=2) + '\n', encoding='utf-8')
    hashes = []
    for path in sorted(stage.rglob('*')):
        if path.is_file():
            hashes.append(f'{digest(path)}  {path.relative_to(stage).as_posix()}')
    (stage / 'SHA256SUMS.txt').write_text('\n'.join(hashes) + '\n', encoding='ascii')
    archive = output / f'{stage.name}.zip'
    if archive.exists():
        raise FileExistsError(archive)
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as packed:
        for path in sorted(stage.rglob('*')):
            if path.is_file():
                packed.write(path, stage.name + '/' + path.relative_to(stage).as_posix())
    checksum = output / (archive.name + '.sha256')
    checksum.write_text(f'{digest(archive)}  {archive.name}\n', encoding='ascii')
    print(json.dumps({'archive': str(archive), 'checksum': str(checksum),
                      'sha256': digest(archive), 'bytes': archive.stat().st_size,
                      'source_commit': commit}))


if __name__ == '__main__':
    main()
