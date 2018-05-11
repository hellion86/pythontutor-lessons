'''
Условие
Последовательность Фибоначчи определяется так:

φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.

По данному числу n определите n-е число Фибоначчи φn.

Эту задачу можно решать и циклом for. 
'''


#Мое решение

r = int(input())

s1 = 1
s2 = 1
if r == 0:
    print(0)
elif r == 2:
    print(1)
elif r == 1:
    print(1)
else:
    for i in range(r-2):
        sum = s1 + s2
        s1 = s2
        s2 = sum
    print(sum)


#Правильное решение
n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)