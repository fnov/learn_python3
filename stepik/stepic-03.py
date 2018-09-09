#Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
#удаляет из него все нечётные значения, а чётные нацело делит на два.
#Функция не должна ничего возвращать, требуется только изменение переданного списка, например:
#lst = [1, 2, 3, 4, 5, 6]
#print(modify_list(lst))  # None
#print(lst)               # [1, 2, 3]
#modify_list(lst)
#print(lst)               # [1]
#
#lst = [10, 5, 8, 3]
#modify_list(lst)
#print(lst)               # [5, 4]

def modify_list1(l):
    l[:] = [i//2 for i in l if not i % 2]
    
def modify_list2(l):
    for x in l[:]:
        if x % 2 == 0:
            l.append(x//2)
        l.remove(x)

def modify_list0(l):
    i = 0
    while i < len(l):
        if not l[i] % 2:  # equal if l[i] % 2 == 0 OR l[i] % 2 != 1
            l[i] = l[i] // 2
        else:
            del l[i]
            i -= 1
        i += 1

lst = [1, 2, 3, 4, 5, 6]
modify_list1(lst)

