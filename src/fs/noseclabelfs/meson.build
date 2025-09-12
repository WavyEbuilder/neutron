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
    'aionoseclabelfs.cil',
    'anoninodenoseclabelfs.cil',
    'autonoseclabelfs.cil',
    'bdevnoseclabelfs.cil',
    'binfmtmiscnoseclabelfs.cil',
    'bpfnoseclabelfs.cil',
    'cinoseclabelfs.cil',
    'confignoseclabelfs.cil',
    'cpusetnoseclabelfs.cil',
    'dosnoseclabelfs.cil',
    'drmnoseclabelfs.cil',
    'efivarnoseclabelfs.cil',
    'fusenoseclabelfs.cil',
    'iso9660noseclabelfs.cil',
    'nfsdnoseclabelfs.cil',
    'nfsnoseclabelfs.cil',
    'nsnoseclabelfs.cil',
    'pidnoseclabelfs.cil',
    'procnoseclabelfs.cil',
    'removablenoseclabelfs.cil',
    'resctrlnoseclabelfs.cil',
    'rpcpipenoseclabelfs.cil',
    'securitynoseclabelfs.cil',
    'selinuxnoseclabelfs.cil',
    'udfnoseclabelfs.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach
