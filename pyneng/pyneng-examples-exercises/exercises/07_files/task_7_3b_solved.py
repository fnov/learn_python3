# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

###

mac_table = 'CAM_table.txt'
mac_lines = []

vlan_num = input('Enter VLAN number: ')

with open(mac_table) as file:
    for line in file:
        if line.count('.') >= 2 and line.strip().startswith(vlan_num):
            mac_lines.append(line.split())

mac_lines.sort()
for line in mac_lines:
    print('{0:>4} {1:>17}   {3}'.format(*line))