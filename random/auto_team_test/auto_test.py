#!/usr/bin/env python3
''' Задача, написать скрипт/программу которая должна

1) осуществлять поиск в iplir.conf и определять содержатся ли в указанной секции id, указанные записи(записей не меньше 1го).
2) В случае положительного результата просто выводить сообщение о успешном завершении.
3) В случае отрицательного результата выводить что именно пошло не так, какую из записей или id не удалось найти.
4) Аргументы содержатся в конфигурационном файле:
    a. path – путь к iplir.conf;  
    b. id – id секция которую будем анализировать
    c. 1 или несколько записей –  которые нужно искать в данной секции(указывается регуляркой)

Пример конфига (conf.txt), для положительного результата
path = /tmp/iplir.conf
id = 0x1620001f
string = "tunnel.*19.0.0.100-19.0.0.110.*19.0.0.100-19.0.0.110"
string1 = "tunnel.*19.0.0.1-19.0.0.1.*19.0.0.1-19.0.0.1"
string2 = "ip.*173.18.0.1"

Пример запуска
<script_name> /tmp/conf.txt'''

import sys
import re

conf = sys.argv[1]
conf_vars = {}
with open(conf) as file:
    for line in file:
        i, j = line.replace('=', '').split()
        conf_vars[i] = j.strip('"')

path = conf_vars.pop('path')
id_num = conf_vars.pop('id')
section_params = []
id_found, id_section = False, False

with open(path) as file:
    for line in file:
        if line.startswith('id=') and id_num in line:
            id_found, id_section = True, True
        elif line.startswith('id=') and id_num not in line:
            id_section = False
            continue
        if id_section:
            section_params.append(line.strip())
        else:
            continue

if id_found:
    for regexp in conf_vars.values():
        if any(re.match(regexp, i) for i in section_params):
            print('Found')
        else:
            print('String "{}" not found in section [id] {}'.format(regexp, id_num))
else:
    print('[id] {} not found in {}'.format(id_num, path))