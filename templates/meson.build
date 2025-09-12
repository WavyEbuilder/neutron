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

mcs_suffix = mcs ? ':s0' : ''
mcs_range_suffix = mcs ? ':s0-s0' : ''

templates_conf_data = configuration_data()
templates_conf_data.set('MCS_SUFFIX', mcs_suffix)
templates_conf_data.set('MCS_RANGE_SUFFIX', mcs_range_suffix)

seusers = configure_file(
    input: 'seusers.in',
    output: 'seusers',
    configuration: templates_conf_data,
)

install_data(
    seusers,
    install_dir: join_paths(get_option('sysconfdir'), 'selinux', selinuxtype),
)

subdir('contexts')
subdir('logins')
