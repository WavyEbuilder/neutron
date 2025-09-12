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

default_contexts = configure_file(
    input: 'default_contexts.in',
    output: 'default_contexts',
    configuration: templates_conf_data,
)

failsafe_context = configure_file(
    input: 'failsafe_context.in',
    output: 'failsafe_context',
    configuration: templates_conf_data,
)

removable_context = configure_file(
    input: 'removable_context.in',
    output: 'removable_context',
    configuration: templates_conf_data,
)

install_data(
    'customizable_types',
    'dbus_contexts',
    default_contexts,
    'default_type',
    failsafe_context,
    removable_context,
    install_dir: join_paths(
        get_option('sysconfdir'),
        'selinux',
        selinuxtype,
        'contexts',
    ),
)

subdir('files')
subdir('users')
