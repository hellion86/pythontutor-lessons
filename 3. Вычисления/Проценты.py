﻿'''
Условие
Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада. Вклад составляет X рублей Y копеек. Определите размер вклада через год.
Программа получает на вход целые числа P, X, Y и должна вывести два числа: величину вклада через год в рублях и копейках. Дробная часть копеек отбрасывается.
'''

p = int(input())
r = int(input())
k = int(input())

r = r * 100 + k
r = r * (p /100) + r

print( r // 100, int(r % 100))