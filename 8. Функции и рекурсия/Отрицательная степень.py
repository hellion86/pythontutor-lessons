'''
Условие
Дано действительное положительное число a и целоe число n.

Вычислите an. Решение оформите в виде функции power(a, n).

Стандартной функцией возведения в степень пользоваться нельзя.
'''

# Мое решение 
a = float(input())
n = int(input())

def power(x,y):
    if y < 0:
        s = 1 / x ** abs(y)
    else:
        s = x ** y
    return s

print(power(a,n))

# Правильное решение
def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res

print(power(float(input()), int(input())))