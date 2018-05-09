'''
Условие
Определите среднее значение всех элементов последовательности, завершающейся числом 0. 
'''

#Мое решение
s = 1
sum = 0
count = 0
while  s != 0:
    s = int(input())
    sum = sum + s 
    count = count + 1
print(sum/(count-1))

#Правльное решение
sum = 0
len = 0
element = int(input())
while element != 0:
    sum += element
    len += 1
    element = int(input())
print(sum / len)