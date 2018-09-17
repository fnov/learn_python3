# -*- coding: utf-8 -*-
'''
Задание 6.1

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

###

ip_input = input('Введите IP-адрес: ')
#ip_input = '254.0.0.1'
ip_octets = [int(i) for i in ip_input.split('.')]

if 0 <= ip_octets[0] < 128:
    ip_class = 'A'
elif 128 <= ip_octets[0] < 192:
    ip_class = 'B'
elif 192 <= ip_octets[0] < 224:
    ip_class = 'C'
elif 224 <= ip_octets[0] < 240:
    ip_class = 'D'
else:
    ip_class = 'E'

if ip_input == '0.0.0.0':
    ip_type = 'unassigned'
elif ip_input == '255.255.255.255':
    ip_type = 'local broadcast'
elif ip_class in 'ABC':
    ip_type = 'unicast'
elif ip_class == 'D':
    ip_type = 'multicast'
else:
    ip_type = 'unused'

print('IP type: {}'.format(ip_type))
