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

cil_files = [
    'editorconffile.cil',
    'environconffile.cil',
    'fstabconffile.cil',
    'hostsconffile.cil',
    'hushloginsconffile.cil',
    'inputrcconffile.cil',
    'localeconffile.cil',
    'logindefsconffile.cil',
    'mimeconffile.cil',
    'motdconffile.cil',
    'protocolsconffile.cil',
    'resolvconffile.cil',
    'selinuxconffile.cil',
    'servicesconffile.cil',
    'skelconffile.cil',
    'tcpwrappersconffile.cil',
    'terminfoconffile.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach
