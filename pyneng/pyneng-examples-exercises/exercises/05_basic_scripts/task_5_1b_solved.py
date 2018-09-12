# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

###

import sys

ip_mask = sys.argv[1].split('/')
#ip_mask = '10.246.245.133/24'.split('/')
ipaddr = [int(i) for i in ip_mask[0].split('.')]

netmask = int(ip_mask[1])
binmask = '1'*netmask + '0'*(32 - netmask)
#byte_len = 8
octmask = [int(binmask[i-8:i], 2) for i in range(8, len(binmask)+1, 8)]

ip_bin = '{:08b}{:08b}{:08b}{:08b}'.format(*ipaddr)
ip_bin_net = ip_bin[:netmask] + '0'*(32 - netmask)
oct_ip_net = [int(ip_bin_net[i-8:i], 2) for i in range(8, len(ip_bin_net)+1, 8)]

out_net = ['Network:',
        '{0:<10}{1:<10}{2:<10}{3:<10}',
        '{0:08b}  {1:08b}  {2:08b}  {3:08b}']
out_mask = ['Mask:',
            '/{mask}',
            '{0:<10}{1:<10}{2:<10}{3:<10}',
            '{0:08b}  {1:08b}  {2:08b}  {3:08b}']

print('\n'.join(out_net).format(*oct_ip_net))
print('\n'.join(out_mask).format(*octmask, mask=netmask))