# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

###

out_info = '''Protocol:              {}
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}'''

file = open('ospf.txt')
for line in file:
    value_list = line.replace(',', '').split()
    if value_list[0] == 'O': value_list[0] = 'OSPF' 
    value_list[2] = value_list[2].strip('[]')
    del value_list[3]
    print(out_info.format(*value_list))
    print()

file.close()
