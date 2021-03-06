'''
Условие
Дано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив его символами "." (каждый элемент массива является строкой из одного символа). Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ. В результате единицы в массиве должны образовывать изображение звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами.
'''

# Мое решение 
n = int(input())
a = [['.' for j in range(n)] for i in range(n)]

for i in range(len(a)):
    for j in range(len(a[i])):
        if i == j:
            a[i][j] = '*'
        a[n//2][j] = '*'
        a[i][n//2] = '*'
        if (i+j == n - 1):
            a[i][j] = '*'


for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end =' ')
    print()   
    

# Правильное решение
n = int(input())
a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i][i] = '*'
    a[n // 2][i] = '*'
    a[i][n // 2] = '*'
    a[i][n - i - 1] = '*'
for row in a:
    print(' '.join(row))