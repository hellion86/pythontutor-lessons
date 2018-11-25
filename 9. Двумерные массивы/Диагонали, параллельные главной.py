'''
Условие
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу. На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.

'''

# Мое решение 
n = int(input())
a = [['.' for j in range(n)] for i in range(n)]

for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = abs(i-j)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end =' ')
    print()

    

# Правильное решение
n = int(input())
a = [[abs(i - j) for j in range(n)] for i in range(n)]
for row in a:
    print(' '.join([str(i) for i in row]))
