# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

###

commands = {'access': access_template, 'trunk': trunk_template}
vlan_choice = {'access': 'Enter VLAN number: ', 'trunk': 'Enter allowed VLANs: '}

mode = input('Enter interface mode (access/trunk): ')
#mode = 'access'
iface = input('Enter interface type and number: ')
#iface = 'Fa0/6'
vlans = input(vlan_choice[mode])
#vlans = '2,3,4,5'

print('interface', iface)
print('\n'.join(commands[mode]).format(vlans))