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
    'binderav.cil',
    'bpfav.cil',
    'capabilityav.cil',
    'fdav.cil',
    'iouringav.cil',
    'ipcav.cil',
    'kernelserviceav.cil',
    'keyav.cil',
    'memprotectav.cil',
    'msgav.cil',
    'perfeventav.cil',
    'socketav.cil',
    'systemav.cil',
    'usernamespaceav.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach
