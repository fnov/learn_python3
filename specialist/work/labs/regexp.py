# labs/regexp.py
import re
# Рейс номер-поезда прибыл/отправился из/в город в время
# [5]: Поезд № 1 3 4
def read_file(filename):
    regexp = r'^Рейс (.+) (прибыл|отправился) (из|в) (.+) в (.+)$'
    pattern = re.compile(regexp, re.I)
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            r = pattern.match(line.strip())
            if r:
                s = f'[{r.group(5)}]: Поезд № {r.group(1)} {r.group(3)} {r.group(4)}'
                data.append(s)
    return data

infile = 'log.txt'
outfile = 'trains.txt'

log = read_file(infile)
# save_file(log)