#!/usr/bin/python

#Напишите код, который принимает целое число и печатает числа, которые следуют до него и после
#него.

n = input()
nextn = int(n) + 1
beforen = int(n) - 1
mesg1 = f'Next number for {n}: {nextn}'
mesg2 = f'Before number for {n}: {beforen}'
print(mesg1)
print(mesg2)
