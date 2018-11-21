'''
Условие
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и выведите результат работы этой функции.
Если вы не знаете, как решить эту задачу, то вы, возможно, не изучали в школе теорему Пифагора. Попробуйте прочитать о ней на Википедии.
'''

# Мое решение 
import math
def distance(a1,b1,a2,b2):
    s = math.sqrt((a1-a2)*(a1-a2) + (b1-b2)*(b1-b2))
    return s

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(distance(x1,y1,x2,y2))

# Правильное решение
from math import sqrt

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(distance(x1, y1, x2, y2))