'''
Задача «Четные индексы»
Условие
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...). 
'''

# Мое решение 
s = input()   
a = s.split()   
for i in range(len(a)):
    if i % 2 == 0:
        print(''.join(a[i]))

# Правильное решение
a = input().split()
for i in range(0, len(a), 2):
    print(a[i])