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

staff_id_user = configure_file(
    input: 'staff.id.in',
    output: 'staff.id',
    configuration: templates_conf_data,
)

sys_id_user = configure_file(
    input: 'sys.id.in',
    output: 'sys.id',
    configuration: templates_conf_data,
)

user_id_user = configure_file(
    input: 'user.id.in',
    output: 'user.id',
    configuration: templates_conf_data,
)

install_data(
    staff_id_user,
    sys_id_user,
    user_id_user,
    install_dir: join_paths(
        get_option('sysconfdir'),
        'selinux',
        selinuxtype,
        'contexts',
        'users',
    ),
)
