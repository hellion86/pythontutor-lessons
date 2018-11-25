'''
Условие
Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке. В левом верхнем углу должна стоять точка.

'''

# Мое решение 
n, m = [int(i) for i in input().split()]
a = [['.' for j in range(m)] for i in range(n)]

for i in range(len(a)):
    for j in range(len(a[i])):
        if i%2 == 0 and j %2 != 0:
            a[i][j] = '*'
        if j%2 == 0 and i %2 != 0:
            a[i][j] = '*'
for row in a:
    print(' '.join(row))
    

# Правильное решение
n, m = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        if (i + j) % 2 == 0:
            a[i].append('.')
        else:
            a[i].append('*')
for row in a:
    print(' '.join(row))