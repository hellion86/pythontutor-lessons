'''
Условие
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:

Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.

Числа, стоящие выше этой диагонали, равны 0.

Числа, стоящие ниже этой диагонали, равны 2.

Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
'''

# Мое решение 
n = int(input())
a = [['0' for j in range(n)] for i in range(n)]

for i in range(len(a)):
    for j in range(len(a[i])):
        if (i+j == n - 1):
            a[i][j] = 1
        elif i+j >= n:
            a[i][j] = 2

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end =' ')
    print()

# Правильное решение
n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i][n - i - 1] = 1
for i in range(n):
    for j in range(n - i, n):
        a[i][j] = 2
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()