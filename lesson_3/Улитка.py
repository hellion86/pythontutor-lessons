﻿'''
Условие
Улитка ползет по вертикальному шесту высотой h метров, поднимаясь за день на a метров, а за ночь спускаясь на b метров. На какой день улитка доползет до вершины шеста?

Программа получает на вход натуральные числа h, a, b.

Программа должна вывести одно натуральное число. Гарантируется, что a>b.
'''

h = int(input())
a = int(input())
b = int(input())
shag = 0
count = 0
while shag <= h:
    shag = shag + a
    count = count + 1
    if shag >= h:
        print(count)
        break
    else:
        shag = shag - b
