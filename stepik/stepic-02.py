#!/usr/bin/python3
"""Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке,
как показано в примере (здесь n=5):

Sample Input:

5

Sample Output:

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9"""

side = int(input())  # длина стороны квадрата
#  заполняем квадратную матрицу нулями
ma = [[0 for j in range(side)] for i in range(side)]
current_side = side  # текущая сторона квадрата
row = 0  # текущее смещение квадрата
num = 1  # текущее число

while row < (side / 2):
    for i in range(current_side):
        ma[row][row + i] = num
        num += 1
    for i in range(current_side - 2):
        ma[1 + row + i][side - 1 - row] = num
        num += 1
    if (side // 2 - row) > 0:
        for i in range(current_side):
            ma[side - 1 - row][side - 1 - i - row] = num
            num += 1
    for i in range(current_side - 2):
        ma[side - 2 - row - i][row] = num
        num += 1
    row += 1
    current_side -= 2

for i in range(len(ma)):
    print(*ma[i])

# optimized

n = int(input())
m = [[0] * n for i in range(n)]
i, j, di, dj = 0, 0, 0, 1

for k in range(n * n):
    m[i][j] = k + 1
    if (not -1 < i + di < n) or (not -1 < j + dj < n) or m[i + di][j + dj] != 0:
        di, dj = dj, -di
    i, j = i + di, j + dj

[print(*i) for i in m]
