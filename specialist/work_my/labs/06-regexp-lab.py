# 06-regexp-lab
# Искать строку вида
# Рейс 365 прибыл из Сасово в 12:56:30
#Представить информацию в виде:
#[время]: Поезд № номер-поезда из/в город
import re

def read_file(fname):
    regexp = r'^Рейс (.+) (прибыл|отправился) (из|в) (.+) в (.+)$'
    pattern = re.compile(regexp, re.I)
    data = []
    with open (fname, 'r' encoding='utf-8') as f:
        for line in f:
            r = pattern.match(line.strip())
            if r:
                print(result.groups())
                s = 'f[{r.group(5)}]: Поезд # {r.group(1)} {r.group(3)} {r.group(4)}'
                data.append(s)
    return data

infile = 'log.txt'
outfile = 'trains.txt'
    
