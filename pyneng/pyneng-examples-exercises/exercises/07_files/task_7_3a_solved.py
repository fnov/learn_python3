# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

###

mac_table = 'CAM_table.txt'
mac_lines = []

with open(mac_table) as file:
    for line in file:
        if line.count('.') >= 2:
            mac_lines.append(line.split())

mac_lines.sort()
for vlan, mac, _, intf in mac_lines:
    print('{:>4} {:>17}   {}'.format(vlan, mac, intf))
