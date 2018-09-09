#n, m, k = (int(i) for i in input().split())  # чтение размеров поля и числа мин
#a = [[0 for j in range(m)] for i in range(n)]  # заполнение поля нулями
#for i in range(k):
#    row, col = (int(i) - 1 for i in input().split())
#    a[row][col] = -1  # расставляем мины
#for i in range(n):
#    for j in range(m):
#        if a[i][j] == 0:  # в этой клетке мины нет, поэтому считаем число мин вокруг
#            for di in range(-1, 2):
#                for dj in range(-1, 2):
#                    ai = i + di
#                    aj = j + dj
#                    # (ai, aj)
#                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
#                        a[i][j] += 1
## вывод результата
#for i in range(n):
#    for j in range(m):
#        if a[i][j] == -1:
#            print('*', end='')
#        elif a[i][j] == 0:
#            print('.', end='')
#        else:
#            print(a[i][j], end='')
#    print()

#Напишите программу, на вход которой подаётся прямоугольная матрица
#в виде последовательности строк, заканчивающихся строкой,
#содержащей только строку "end" (без кавычек)
#Программа должна вывести матрицу того же размера,
#у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы
#на позициях(i-1, j),(i+1, j), (i, j-1), (i, j+1).
#У крайних символов соседний элемент находится с противоположной стороны матрицы.
#В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
#
#Sample Input 1:
#
#9 5 3
#0 7 -1
#-5 2 9
#end
#
#Sample Output 1:
#
#3 21 22
#10 6 19
#20 16 -1

ll = []
while True:
    ss = input()
    if ss == 'end':
        break
    else:
        ll.append([int(s) for s in ss.split()])

m = len(ll)       
for i in range(m):
    n = len(ll[i])
    for j in range(n):
        x = ll[i-1][j] + ll[i-m+1][j] + ll[i][j-1] + ll[i][j-n+1]
        print(x, end=' ')
    print()

    