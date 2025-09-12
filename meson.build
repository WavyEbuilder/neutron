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

project('neutron', meson_version: '>= 1.3.0', version: '0.1')

polvers = get_option('polvers')
selinuxtype = meson.project_name()
mcs = get_option('mcs')
systemd = get_option('systemd')

policy_sources = []

subdir('src')
subdir('templates')

policy = custom_target(
    'policy',
    output: ['policy.@0@'.format(polvers), 'file_contexts'],
    input: policy_sources,
    command: [
        'secilc',
        '-OM',
        mcs ? ['true'] : ['false'],
        '--policyvers=@0@'.format(polvers),
        '@INPUT@',
    ],
    install: true,
    install_dir: [
        join_paths(get_option('sysconfdir'), 'selinux', selinuxtype, 'policy'),
        join_paths(
            get_option('sysconfdir'),
            'selinux',
            selinuxtype,
            'contexts',
            'files',
        ),
    ],
    install_mode: 'rw-------',
    build_by_default: true,
)

# Hack to work around lack of meson support for different
# install_modes for mutiple outputs in custom_target
meson.add_install_script(
    'chmod',
    '644',
    join_paths(
        get_option('prefix'),
        get_option('sysconfdir'),
        'selinux',
        selinuxtype,
        'contexts',
        'files',
        'file_contexts',
    ),
)
