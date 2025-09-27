# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

cil_files = [
    'kmod.cil',
    'ldconfig.cil',
    'sysctl.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

if systemd
    policy_sources += files('kmodsystemd.cil')
endif
