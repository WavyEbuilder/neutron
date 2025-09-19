# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

test(
    'sechecker',
    find_program('sechecker'),
    args: [
        meson.project_source_root() / 'test/sechecker.ini',
        policy[0], # policy.$polvers
    ],
    depends: policy,
)
