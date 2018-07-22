#!/usr/bin/env python
# 根据 IPy 源码测试实现的方法
from IPy import IP
from IPy import parseAddress
################ IP 类 ######################
"""
方法1：net
实现：作为 IP 对象，返回网络基（第一）地址
说明：等价于 IP[0]
测试：IP('10.0.0.0/8').net()

"""
#ip_s = input("Please input an IP or net-range: ")
ip_s = "10.0.0.0/8"
ips = IP(ip_s)
print('net: %s' % ips.net())


"""
方法2：broadcast
实现：作为 IP 对象，返回网络广播（最后）地址
说明：等价于 IP[-1]
测试: IP('10.0.0.0/8').broadcast()
"""
print('broadcast: %s' % ips.broadcast())

"""
方法3：netmask
实现：作为 IP 对象，返回网络掩码地址
测试：IP('10.0.0.0/8').netmask()
"""
print('netmask: %s'%ips.netmask())

"""
方法4：reverseNames
实现：返回地址反向解析
测试：  IP('213.221.113.87/32').reverseNames()
        IP('213.221.112.224/30').reverseNames()
        IP('127.0.0.0/24').reverseNames()
        IP('127.0.0.0/23').reverseNames()
        IP('127.0.0.0/16').reverseNames()
        IP('127.0.0.0/15').reverseNames()
        IP('128.0.0.0/8').reverseNames()
        IP('128.0.0.0/7').reverseNames()
        IP('::1:2').reverseNames()
"""
print("============ reverseNames ============")
print('reverNames: %s' % IP('213.221.113.87/32').reverseNames())
print('reverNames: %s' % IP('213.221.112.224/30').reverseNames())
print('reverNames: %s' % IP('127.0.0.0/24').reverseNames())
print("======================================")

"""
方法5：make_net
实现：根据给定的网络掩码将单个 IP 地址转换成网络规范格式
测试：IP('127.0.0.1').make_net('255.0.0.0')
"""
print('make_net: %s' % IP('127.0.0.1').make_net('255.0.0.0'))

################ parseAddress 类 ######################
"""
方法：parseAddress
实现：解析一个字符串并返回其相对应的 IP 地址（整数）以及可能版本
"""
def testParseAddress(address):
    ip, version = parseAddress(address)
    print(("%s (IPv%s)" % (ip, version)))

print("================== tesParseAddress ===================")
print('parseAddress: %s' % testParseAddress('123.123.123.123') ) #IPv4
print('parseAddress: %s' % testParseAddress('1080:0::8:800:200C:417A') ) #IPv6
print("======================================================")

######################## 其他 ########################
"""
测试：ips = IP('10.0.0.0/8')
"""
print('subnet: %s' % len(ips)) #输出网络子网数
print('hexadecimal: %s' % ips.strHex()) #输出十六进制地址
print('binary ip: %s' % ips.strBin()) #输出二进制地址
print('iptype: %s' % ips.iptype()) #输出地址类型，如 Private、Public、LoopBack等

