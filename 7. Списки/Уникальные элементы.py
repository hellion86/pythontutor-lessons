'''
Условие
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
'''

# Мое решение 
a = [int(s) for s in input().split()]

for i in a:
    if a.count(i) == 1:
        print(i,end=' ')
   

# Правильное решение
a = [int(s) for s in input().split()]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=' ')