#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

import itertools
import subprocess
import sys

CONFIG_MATRIX = {
    "mcs": ["true", "false"],
    "systemd": ["true", "false"],
    "polvers": ["33"],  # github ci kernel is too old for polvers 34
}


def run_command(cmd, cwd=None):
    try:
        subprocess.run(cmd, cwd=cwd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command `{' '.join(cmd)}` failed", file=sys.stderr)
        sys.exit(e.returncode)


def main():
    keys = list(CONFIG_MATRIX.keys())

    for values in itertools.product(*(CONFIG_MATRIX[k] for k in keys)):
        combo = dict(zip(keys, values))

        build_dir = "build_" + "_".join([f"{k}_{v}" for k, v in combo.items()])
        meson_opts = [f"-D{k}={v}" for k, v in combo.items()]

        print(f"Testing: {meson_opts}")

        # --wipe shouldn't really be needed (as build_dir is different for each
        # combination), but it doesn't hurt.
        run_command(["meson", "setup", build_dir, "--wipe"] + meson_opts)
        run_command(["meson", "compile", "-C", build_dir])
        run_command(["meson", "test", "-C", build_dir, "--print-errorlogs"])


if __name__ == '__main__':
    sys.exit(main())
