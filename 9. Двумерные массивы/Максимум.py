'''
Условие
Найдите индексы первого вхождения максимального элемента. Выведите два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве. Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.

Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.
'''

# Мое решение 
n,m = input().split()

a = []
for i in range(int(n)):
    a.append([int(j) for j in input().split()])
max = a[0][0]
index1 = 0
index2 = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] > max:
            max = a[i][j]
            index1 = i
            index2 = j
        
        
print(index1,index2)    
    

# Правильное решение
n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
best_i, best_j = 0, 0
curr_max = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > curr_max:
            curr_max = a[i][j]
            best_i, best_j = i, j
print(best_i, best_j)