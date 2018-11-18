'''
Условие
Определите сумму всех элементов последовательности, завершающейся числом 0. В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно. 
'''

#Мое решение
s = 1
sum = 0
while  s != 0:
    s = int(input())
    sum = sum + s 
print(sum)

#Правильное решение
sum = 0
element = int(input())
while element != 0:
    sum += element
    element = int(input())
print(sum)
