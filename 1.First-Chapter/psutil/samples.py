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

"""