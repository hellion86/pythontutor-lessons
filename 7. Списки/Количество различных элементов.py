'''
Условие
Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
'''

# Мое решение 
a = [int(s) for s in input().split()]

a1=1
for i in range(1, len(a)):
    if a[i-1] != a[i]:
        a1 = a1 + 1
print(a1)
 
# Правильное решение
a = [int(i) for i in input().split()]
num_distinct = 1
for i in range(0, len(a) - 1):
    if a[i] != a[i + 1]:
        num_distinct += 1
print(num_distinct)
 