'''
Условие
Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.

Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.

Решение оформите в виде функции swap_columns(a, i, j).
'''

#Мое решение
def swap(a,i,j):
    for s in range(len(a)):
        a[s][int(i)],a[s][int(j)] = a[s][int(j)],a[s][int(i)]

n,m = input().split()
a = []
for i in range(int(n)):
    a.append([int(j) for j in input().split()])
f,g = input().split()

swap(a,f,g)
   
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
	
	
#Правильное решение
def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]

n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]
swap_columns(a, i, j)
print('\n'.join([' '.join([str(i) for i in row]) for row in a]))