# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

cil_files = [
    'dbus.cil',
    'nss.cil',
    'openssh.cil',
    'pam.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('openssh')
subdir('pam')
subdir('utillinux')
