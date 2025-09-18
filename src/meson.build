# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

cil_files = [
    'agent.cil',
    'anoninode.cil',
    'dev.cil',
    'file.cil',
    'fs.cil',
    'invalid.cil',
    'kernel.cil',
    'misc.cil',
    'net.cil',
    'selinux.cil',
    'subj.cil',
    'sys.cil',
    'unlabeled.cil',
    'user.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('agent')
subdir('anoninode')
subdir('dev')
subdir('file')
subdir('fs')
subdir('misc')
subdir('net')
subdir('selinux')
subdir('sys')
subdir('user')
