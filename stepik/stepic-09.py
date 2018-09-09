d_class = {i:[0, 0] for i in range(1, 12)} 

with open('dataset_3363_3.txt', 'r', encoding='utf-8') as f_in:
    for line in f_in:
        temp_l = line.split('/t')
        d_class[temp_l[0]] += temp_l[2]
        d_class[temp_l[1]] += 1

for i, j in d_class.items():
    if j[0] == 0:
        print(i, '-')
    else:
        j[0] /= j[1]
        print(i, j[0])