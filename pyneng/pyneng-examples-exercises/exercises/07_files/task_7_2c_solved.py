# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

###

import sys

config = sys.argv[1]
#config = 'config_sw1.txt'
config_clean = sys.argv[2]
#config_clean = 'config_sw1_cleared.txt'

with open(config, 'r') as src, open(config_clean, 'w') as dst:
    for line in src:
        if not any(i in line for i in ignore):
            dst.write(line)