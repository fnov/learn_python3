while True:
    count = int(input('Введите число ворон: '))
    if count < 0:
        break
    out = 'На ветке {} ворон'.format(count)
    suffix = ''
    if count%100 <= 11 or count%100 >= 14:
        n = count%10
        if n == 1:
            suffix = 'а'
        elif n == 2 or n == 3 or n == 4:
            suffix = 'ы'
    print(out + suffix)
