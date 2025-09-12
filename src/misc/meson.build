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

mcs_enabled = mcs ? 'true' : 'false'

cil_conf_data = configuration_data()
cil_conf_data.set('MCS_ENABLED', mcs_enabled)

conf_cil = configure_file(
    input: 'conf.cil.in',
    output: 'conf.cil',
    configuration: cil_conf_data
)

policy_sources += conf_cil

cil_files = [
    'av.cil',
    'default.cil',
    'isid.cil',
    'map.cil',
    'mls.cil',
    'modular.cil',
    'obj.cil',
    'perm.cil',
    'silenced.cil',
    'unconfined.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('av')
subdir('constrain')
subdir('xperm')
