# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.

Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
а включая последний.

Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последни
й октет адреса.

Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов


Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
'''

###

import subprocess
import ipaddress

def check_ip_availability(ip_address_range):
    """
    Ping IP addresses in list and return 2 lists
    of alive and unreachable adresses:
    """
    
    def check_ip_address(ip):
        """
        Ping IP address and append to list 
        of alive or unreachable adresses:
        """
        reply = subprocess.run(['ping', '-c', '3', '-n', ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,)
        if reply.returncode == 0:
            alive_ip_list.append(ip)
        else:
            unreach_ip_list.append(ip)

    alive_ip_list = []
    unreach_ip_list = []
    
    if '-' in ip_address_range:
        ip1, ip2 = ip_address_range.split('-')
        ip_start = ipaddress.ip_address(ip1)
        try:
            ip_last = ipaddress.ip_address(ip2)
        except ValueError:
            ip_dif = int(ip2) - int(ip1.split('.')[3])
            ip_last = ip_start + ip_dif

        while ip_start <= ip_last:
            check_ip_address(str(ip_start))
            ip_start += 1
    else:
        check_ip_address(ip_address_range)
        
    return alive_ip_list, unreach_ip_list



a_list, u_list = check_ip_availability('192.168.1.67-68')
a1_list, u1_list = check_ip_availability('192.168.1.67-192.168.1.70')
