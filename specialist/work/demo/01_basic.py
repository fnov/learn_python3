# demo/basic.py
n1 = input('Введите первое число: ')
n2 = input('Введите второе число: ')
#s = n1 + ' + ' + n2 + ' = ' + str(int(n1)+int(n2))
result = int(n1) + int(n2)
# s = '{} + {} = {}'.format(n1, n2, result)
# s = '{1} + {0} = {2}'.format(n1, n2, result)
# s = '{op1} + {op2} = {sum}'.format(op1=n1, op2=n2, sum=result)
s = f'{n1} + {n2} = {result}'
print(s)
