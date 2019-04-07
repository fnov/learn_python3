# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = 'AAAA:BBBB:CCCC'

###

int_bin_list = [int(i, 16) for i in MAC.split(':')]
fmt = '{0:08b}{1:08b}{2:08b}'
mac_bin = fmt.format(*int_bin_list)
print(mac_bin)