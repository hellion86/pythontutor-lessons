'''Условие
Даны три целых числа. Выведите значение наименьшего из них.
'''

a = int(input())
b = int(input())
c = int(input())

if a <= b and a <= c:
    print(str(a))
elif b <= a and b <= c:
    print(str(b))
else:
    print(str(c))

