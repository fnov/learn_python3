# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

###

import subprocess

def check_ip_addresses(ip_address_list):
    """
    Ping IP addresses in list and return 2 lists
    of alive and unreachable adresses:
    """
    alive_ip_list = []
    unreach_ip_list = []
    
    for ip_addr in ip_address_list:
        reply = subprocess.run(['ping', '-c', '3', '-n', ip_addr],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,)
        if reply.returncode == 0:
            alive_ip_list.append(ip_addr)
        else:
            unreach_ip_list.append(ip_addr)
    return alive_ip_list, unreach_ip_list


a_list, u_list = check_ip_addresses(('8.8.8.8', '8.8.4.4', 'a', 'b'))
