'''
Условие
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента
'''

# Мое решение 
a = input().split()
for i in range(1, len(a)):
    if int(a[i]) > int(a[i-1]):
        print(a[i], end= ' ')

# Правильное решение
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])
