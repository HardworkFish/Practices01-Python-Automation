#!/usr/bin/env python
# Changed Time：2018-07-22 9:40
from IPy import IP

ip_s = input('Please input an IP or net-range: ') #接收用户输入参数为IP地址或网段地址
ips = IP(ip_s)


if len(ips) > 1: #为一个网络地址 以“192.168.1.0/24”为例
    print('net: %s' % ips.net()) #输出网络地址
    print('netmask: %s' % ips.netmask()) #输出网络掩码
    print('broadcast: %s' % ips.broadcast()) #输出网络广播地址
    print('reverse address: %s' % ips.reverseNames()[0]) #输出地址反向解析
    print('subnet: %s' % len(ips)) #输出网络子网数
else:
    print('reverse address: %s' % ips.reverseNames()[0]) #输出IP反向解析 以“192.168.1.20”

print('hexadecimal: %s' % ips.strHex()) #输出十六进制地址
print('binary ip: %s' % ips.strBin()) #输出二进制地址
print('iptype: %s' % ips.iptype()) #输出地址类型，如 Private、Public、LoopBack等

