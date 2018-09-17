# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

###

ip_input = input('Введите IP-адрес: ')
#ip_input = '254.0.0.256'
correct_ip = False

if ip_input.count('.') == 3:
    ip_octets = [int(i) for i in ip_input.split('.') if i.isdigit()]
    if len(ip_octets) == 4:
        for i in ip_octets:
            if i in range(0,256):
                correct_ip = True
            else:
                correct_ip = False
                break

if not correct_ip:
    print('Incorrect IPv4 address')
else:
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
