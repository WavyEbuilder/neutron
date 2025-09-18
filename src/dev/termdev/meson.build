# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

cil_files = [
    'ptytermdev.cil',
    'serialtermdev.cil',
    'systermdev.cil',
    'usertermdev.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('ptytermdev')
subdir('serialtermdev')
subdir('systermdev')
subdir('usertermdev')
