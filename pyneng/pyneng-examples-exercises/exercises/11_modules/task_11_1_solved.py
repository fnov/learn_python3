# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def parse_cdp_neighbors(output):
    out_dict = {}
    lines = output.split('\n')
    host = lines[0].split('>')[0]
    for line in lines:
        if line.startswith('Device ID'):
            break
    i = lines.index(line)
    setup_list =[j.split() for j in lines[i+1:] if j]
    for device, if_local_type, if_local_num, *other, port_type, port_num in setup_list:
        t1 = (host, if_local_type+if_local_num)
        t2 = (device, port_type+port_num)
        out_dict[t1] = t2
    return out_dict

with open('sw1_sh_cdp_neighbors.txt') as file:
    cdp_dict = parse_cdp_neighbors(file.read())