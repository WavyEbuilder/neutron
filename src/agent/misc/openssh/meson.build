# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

cil_files = [
    'opensshclient.cil',
    'opensshkeygen.cil',
    'opensshserver.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

if systemd
    policy_sources += files('opensshserversystemd.cil')
endif
