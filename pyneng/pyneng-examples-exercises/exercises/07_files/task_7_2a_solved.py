#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

###

import sys

config = sys.argv[1]
#config = 'config_sw1.txt'

with open(config) as file:
    for line in file:
        if line.startswith('!'):
            continue
        elif any(i in line for i in ignore):
            continue
        else:
            print(line.rstrip())