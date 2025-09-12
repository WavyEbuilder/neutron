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
    'acpiprocfile.cil',
    'asoundprocfile.cil',
    'bootconfigprocfile.cil',
    'buddyinfoprocfile.cil',
    'busprocfile.cil',
    'cgroupsprocfile.cil',
    'cmdlineprocfile.cil',
    'consolesprocfile.cil',
    'cpuinfoprocfile.cil',
    'cpuprocfile.cil',
    'cryptoprocfile.cil',
    'devicesprocfile.cil',
    'diskstatsprocfile.cil',
    'dmaprocfile.cil',
    'driverprocfile.cil',
    'dynamicdebugprocfile.cil',
    'execdomainsprocfile.cil',
    'fbprocfile.cil',
    'filesystemsprocfile.cil',
    'fsprocfile.cil',
    'interruptsprocfile.cil',
    'iomemprocfile.cil',
    'ioportsprocfile.cil',
    'irqprocfile.cil',
    'jffs2bbcprocfile.cil',
    'kallsymsprocfile.cil',
    'kcoreprocfile.cil',
    'keysprocfile.cil',
    'keyusersprocfile.cil',
    'kmsgprocfile.cil',
    'kpagecgroupprocfile.cil',
    'kpagecountprocfile.cil',
    'kpageflagsprocfile.cil',
    'latencystatsprocfile.cil',
    'loadavgprocfile.cil',
    'lockdepchainsprocfile.cil',
    'lockdepprocfile.cil',
    'lockdepstatsprocfile.cil',
    'locksprocfile.cil',
    'lockstatprocfile.cil',
    'mdstatprocfile.cil',
    'meminfoprocfile.cil',
    'miscprocfile.cil',
    'modulesprocfile.cil',
    'mptprocfile.cil',
    'mtdprocfile.cil',
    'mtrrprocfile.cil',
    'netprocfile.cil',
    'pagetypeinfoprocfile.cil',
    'partitionsprocfile.cil',
    'pressureprocfile.cil',
    'scheddebugprocfile.cil',
    'schedstatprocfile.cil',
    'scsiprocfile.cil',
    'slabinfoprocfile.cil',
    'softirqsprocfile.cil',
    'statprocfile.cil',
    'swapsprocfile.cil',
    'sysctlfile.cil',
    'sysctlprocfile.cil',
    'sysrqtriggerprocfile.cil',
    'sysvipcprocfile.cil',
    'timerlistprocfile.cil',
    'ttyprocfile.cil',
    'uptimeprocfile.cil',
    'versionprocfile.cil',
    'vmallocprocfile.cil',
    'vmstatprocfile.cil',
    'zoneinfoprocfile.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('sysctlfile')
