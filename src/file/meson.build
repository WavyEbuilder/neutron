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
    'authfile.cil',
    'bootfile.cil',
    'bootflagfile.cil',
    'certfile.cil',
    'conffile.cil',
    'datafile.cil',
    'devfile.cil',
    'homefile.cil',
    'hugetlbfsfile.cil',
    'mqueuefsfile.cil',
    'runfile.cil',
    'secfile.cil',
    'tmpfile.cil',
    'tmpfsfile.cil',
    'userfile.cil',
    'varfile.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('authfile')
subdir('conffile')
subdir('datafile')
subdir('homefile')
subdir('hugetlbfsfile')
subdir('misc')
subdir('mqueuefsfile')
subdir('runfile')
subdir('tmpfile')
subdir('tmpfsfile')
subdir('varfile')
