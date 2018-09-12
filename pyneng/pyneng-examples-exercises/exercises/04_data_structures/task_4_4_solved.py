# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

###

def get_vlans_list(string):
    i = string.index('1')
    return [int(j) for j in string[i:].split(',')]

set1 = set(get_vlans_list(command1))
set2 = set(get_vlans_list(command2))
vlans_repeat = list(set1 & set2)