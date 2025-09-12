#! /usr/bin/env python3

# neutron - Next-generation system SELinux policy
# Copyright (C) 2025 Rahul Sandhu <nvraxn@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License, as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse
import sys

from pathlib import Path


def generate(directory: Path, recursive: bool = False):
    sources = sorted([f.name for f in directory.glob('*.cil')])

    out = []
    out.append(r"""# neutron - Next-generation system SELinux policy
# Copyright (C) 2025 Rahul Sandhu <nvraxn@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License, as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
""")

    if sources:
        out.append('cil_files = [')
        for f in sources:
            out.append(f"    '{f}',")
        out.append(']')
        out.append('')
        out.append("foreach file : cil_files")
        out.append("    policy_sources += files(file)")
        out.append("endforeach")

    subdirs = sorted([
        d.name for d in directory.iterdir() if d.is_dir() and not d.name.startswith('.')
    ])

    if sources and subdirs:
        out.append('')

    for sub in subdirs:
        out.append(f"subdir('{sub}')")

    file = directory / 'meson.build'
    with file.open('w') as f:
        f.write('\n'.join(out))
        f.write('\n')

    if recursive:
        for sub in subdirs:
            generate(directory / sub, recursive=True)


def main() -> int:
    parser = argparse.ArgumentParser(
        description='Generate meson.build from policy source directories')
    parser.add_argument('-d',
                        '--directory',
                        default='.',
                        help='Directory to operate under (default: current)')
    parser.add_argument('-r',
                        '--recursive',
                        action='store_true',
                        help='Operate recursively')
    args = parser.parse_args()

    dir_path = Path(args.directory).resolve()

    if not dir_path.is_dir():
        print(f"Error: '{dir_path}' is not a directory", file=sys.stderr)
        return 1

    generate(dir_path, recursive=args.recursive)

    return 0


if __name__ == '__main__':
    sys.exit(main())
