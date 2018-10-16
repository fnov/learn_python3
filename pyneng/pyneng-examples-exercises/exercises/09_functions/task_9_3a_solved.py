# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config):
    access_dict, trunk_dict = {}, {}
    
    with open(config) as file:
        for line in file:
            if '!' in line:
                continue
            elif 'interface' in line:
                iface = line.split()[-1]
                continue
            if 'mode access' in line:
                access_dict[iface] = 1  # default vlan
            elif 'access vlan' in line:
                vlan = line.split()[-1]
                access_dict[iface] = int(vlan)
            elif 'allowed vlan' in line:
                vlans = line.split()[-1]
                trunk_dict[iface] = [int(vlan) for vlan in vlans.split(',')]
    
    return access_dict, trunk_dict


access_template, trunk_template = get_int_vlan_map('config_sw2.txt')