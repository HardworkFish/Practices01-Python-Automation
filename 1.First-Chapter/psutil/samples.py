#!/usr/bin/env python
import psutil
"""
概要：psutil 可以获取系统性能信息
说明：采集系统的基本性能信息包括 CPU、内存、磁盘、网络等
测试环境：win10
项目地址：https://github.com/giampaolo/psutil
官网介绍地址：https://pypi.org/project/psutil
使用文档：http://psutil.readthedocs.io/en/latest

"""

"""
(1)CPU 信息
下面的每个属性表示 CPU 在给定模式下花费的时间（秒/s)。属性可用性因平台而异。
    percpu=False(默认)，不同平台下各共同性能指标情况：
        1.user：执行用户进程的时间
        2.system:执行内核进程和中断的时间
        3.idle:CPU 处在 idle 状态（即空闲状态下）的时间
    下面的指标依平台而异：
        4.nice(Unix):在用户模式下执行的 niced （优先级）进程所花费的时间；在 Linux 上，这还包括了 guest_nice 时间
        5,iowait(Linux):等待 I/O 完成而使 CPU 处于 idle（空闲）状态的时间
        6.irq(Linux,BSD):服务硬件中断所发费的时间
        7.softirq(Linux):服务软件中断所发费的时间
        8.steal（Linux 2.6.11+）:在虚拟化环境中运行其他操作系统所花费的时间
        9.guest（Linux 2.6.24+）:在 Linux 内核的控制下为客户端运行虚拟 CPU 所花费的时间
        10.guest_nice（Linux 3.2.0+）:运行 niced guest 虚拟机所花费的时间（Linux 内核控制下的）
        11.interrupt（Windows）:硬件服务中断所花费的时间（类似于 Unix 上的 “irq”）
        12.dpc（Windows）:服务延迟过程调用（DPC）所花费的时间；DPCs 中断比标准中断优先级低的中断
        
    当percpu=True 时，返回所有逻辑CPU信息列表。
    实例：scputimes(user=2403.046875, system=1970.296875, idle=10414.640625, interrupt=84.859375, dpc=42.15625)  
    
    
"""
#CPU 使用时间信息
print('cpu_time: %s' % str(psutil.cpu_times()))
print('cpu_time: %s' % str(psutil.cpu_times(percpu=True))) #显示所有逻辑 CPU 信息
print('user_use_time %s' % psutil.cpu_times().user) #获取单项数据信息，显示用户 user 的CPU 使用时间

print('cpu_logical_count: %s' % psutil.cpu_count()) #获取逻辑 CPU 个数,默认 logical=True
print('cpu_physic_count: %s' % psutil.cpu_count(logical=False)) #获取物理 CPU 个数

# CPU 频率
# 分别输出当频率、最小频率以及最大频率（赫兹/HZ）
print('cpu_freq: %s' % str(psutil.cpu_freq()))

#当前指定范围的 CPU 利用率
print('cpu_percent: %s' % psutil.cpu_percent())

#统计 CPU 各个信息
"""
1.ctx_switchs:启动后上下文切换次数（自愿+非自愿）
2.interrupts:自引导以来的中断次数
3.soft_interrupts:自引导以来的软件中断次数
4.syscalls：自引导以来的系统调用次数
"""
print('cpu_status: %s' % str(psutil.cpu_stats()))


"""
（2）内存信息
virtual_memory 虚拟内存统计信息
下面的每个属性表示内存在给定模式下的利用率相关信息（字节/Byte）。属性可用性因平台而异。
    1.total：总物理内存
    2.available：在系统不需要进入交换的情况可以立即供给进程的内存
    3.used：已使用的内存
    4.free：空闲内存
    5.active（Unix）：当前正在使用或最近使用的内存，因此它位于 RAM 中
    6.inactive（Unix）：标记为未使用的内存
    7.buffers（Linux，BSD）：缓存文件系统元数据之类的东西
    8.cached（Linux，BSD）：各种缓存
    9.shared（Linux，BSD）：可由多个进程同时访问的内存
    10.slab（Linux）：内核数据结构缓存
    11.wired（BSD，masOS）：标记为始终保留在 RAM 中的内存。它永远不会移动到磁盘
已使用内存和可用内存的总和并不一定等于总内存大小

sawp_memory 交换内存统计信息
    1.total：总交换内存（字节/Byte）
    2.used：已用于交换的 swap 内存（字节/Byte）
    3.free：自由交换的可用内存（字节/Byte）
    4.percentage：(total - available) / total * 100 计算值，使用率
    5.sin:系统从磁盘换入的字节数（累计）
    6.sout:系统从磁盘换出的字节数（累计）
    

"""
# 虚拟内存
print('virtual_memory：%s' % str(psutil.virtual_memory()))

#获取交换分区信息
print('swap_memory：%s' % str(psutil.swap_memory()))

"""
（3）磁盘信息
在系统的所有磁盘信息中，更加关注磁盘的利用率及IO信息，其中磁盘利用率使用 psutil.disk_usage 方法获取。
磁盘 IO 信息包括 read_count（读IO数）、write_count（写IO数）、read_bytes（IO读字节数）、write_bytes（IO写字节数）、read_time（磁盘读时间）、write_time（磁盘写时间）等。
这些 IO 信息可以使用 psutil.disk_io_counters() 获取，具体见下面的操作例子。

"""

print('disk_partitions: %s'%str(psutil.disk_partitions()))    #使用psutil.disk_partitions方法获取磁盘完整信息
print('disk_usage: %s' % str(psutil.disk_usage('/'))) #使用psutil.disk_usage方法获取分区(参数)的使用情况
print('disk_io_counters: %s' % str(psutil.disk_io_counters())) #使用psutil.disk_io_counters获取硬盘总的IO个数、读写信息
print('disk_io_counters: %s'% str(psutil.disk_io_counters(perdisk=True))) # “perdisk=True”参数获取单个分区IO个数、读写信息

"""
(4)网络信息
系统的网络信息与磁盘IO类似，涉及几个关键点，包括bytes_sent（发送字节数）、bytes_recv=28220119（接收字节数）、packets_sent=200978（发送数据包数）、packets_recv=212672（接收数据包数）等。
这些网络信息使用 psutil.net_io_counters()方法获取，
"""
import datetime
print('net_io_counters: %s' % str(psutil.net_io_counters()))  #使用psutil.net_io_counters获取网络总的IO信息，默认pernic=False
print('each_net_io_counters: %s'% str(psutil.net_io_counters(pernic=True)))  #pernic=True输出每个网络接口的IO信息


"""
（5）其他系统信息
除了前面介绍的几个获取系统基本信息的方法，psutil 模块还支持获取用户登录、开机时间等信息。
"""
print('users:%s' % str(psutil.users()))    #使用psutil.users方法返回当前登录系统的用户信息
print('boot_time:%s' % str(psutil.boot_time()))    #使用psutil.boot_time方法获取开机时间，以Linux时间戳格式返回
print('format_boot_time: %s'% (datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))) # 转换成自然时间格式


"""
1.1.2 系统进程管理方法

获得当前系统的进程信息，可以得知应用程序的运行状态，包括进程的启动时间、查看或设置CPU亲和度、内存使用率、IO信息、socket连接、线程数等，
这些信息可以呈现出指定进程是否存活、资源利用情况，为开发人员的代码优化、问题定位提供很好的数据参考。
"""

"""
（1）进程信息
psutil模块在获取进程信息方面也提供了很好的支持，包括使用psutil.pids()方法获取所有进程PID，
使用psutil.Process()方法获取单个进程的名称、路径、状态、系统资源利用率等信息
"""
print('pids: %s' % str(psutil.pids()))#列出所有进程PID
p = psutil.Process(476)  #实例化一个Process对象，参数为一进程PID
print('pid_name: %s' % p.name())  #进程名
print('pid_status: %s' % p.status()) #进程状态
print('pid_create_time: %s' % p.create_time()) #进程创建时间
print('pid_memory_percent: %s' % p.memory_percent()) #进程内存利用率
print('pid_io_counters: %s' % str(p.io_counters())) #进程IO信息，包括读写IO数及字节数
print('pid_num_threads: %d'% p.num_threads()) #进程开启线程数


"""
（2）popen类的使用
psutil提供的popen类的作用是获取用户启动的应用程序进程信息，以便跟踪程序进程的运行状态。
"""
from subprocess import  PIPE

#通过psutil的Popen方法启动的应用程序，可以跟踪该程序运行的所有相关信息
p = psutil.Popen(["C:/Users/Micky/AppData/Local/Programs/Python/Python35/python", "-c", "print('hello')"], stdout=PIPE)
print('p_name: %s' % p.name())
print('p_username: %s' % p.username())
print('p_cou_time: %s' % p.cpu_times)