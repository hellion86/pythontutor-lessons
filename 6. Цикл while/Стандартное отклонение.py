'''
Условие

Дана последовательность натуральных чисел x1
, x2, ..., xn. Стандартным отклонением называется величина
σ=(x1−s)2+(x2−s)2+…+(xn−s)2n−1−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−√
где s=x1+x2+…+xnn

 — среднее арифметическое последовательности.

Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.
'''

#Мое решение
import math
s = 1
sum = 0
j = 0
l = []
while s != 0:
    
    s = int(input())
    l.append(s)
    sum = sum + s
    j = j + 1
  
sr = sum / (j - 1)
j = len(l)-2
sum1 = 0
for i in range(len(l)-1):
    sum1 = ((l[i] - sr) * (l[i] - sr))/j + sum1 
 
print(math.sqrt(sum1))
 

#Правильный вариант
from math import sqrt

partial_sum = 0
partial_sum_squares = 0
x_i = int(input())
n = 0
while x_i != 0:
    n += 1
    partial_sum += x_i
    partial_sum_squares += x_i ** 2
    x_i = int(input())
print(sqrt((partial_sum_squares - partial_sum ** 2 / n) / (n - 1)))