'''
Условие
Последовательность состоит из натуральных чисел и завершается числом 0. Определите значение наибольшего элемента последовательности. 
'''

#Мое решение
s = 0

element = int(input())
while element != 0:
    if s <= element:
        s = element
    element = int(input())
print(s)

#Правльное решение
max = 0
element = -1
while element != 0:
    element = int(input())
    if element > max:
        max = element
print(max)