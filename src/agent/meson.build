# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

cil_files = [
    'hybridagent.cil',
    'sysagent.cil',
    'useragent.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('hybridagent')
subdir('misc')
subdir('sysagent')

if systemd
    policy_sources += files('hybridagentsystemd.cil')
    policy_sources += files('sysagentsystemd.cil')
endif
