'''
Условие
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
'''

# Мое решение 
a = [int(s) for s in input().split()]
count=0
for i in range(0,len(a)):
    for j in range(i+1, len(a)):
        if a[j] == a[i]:
            count = count + 1
print(count)

# Правильное решение
a = [int(s) for s in input().split()]
counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            counter += 1
print(counter)