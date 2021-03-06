'''
Условие
Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию с индексом k элемент, равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
Поскольку при этом количество элементов в списке увеличивается, после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.

Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка.
'''

# Мое решение 
a = [int(s) for s in input().split()]
d = [int(b) for b in input().split()]

s1 = int(d[0])
s2 = int(d[1])
a.append(s2)
a1=0
for i in range(len(a)-1,s1,-1):
  a1 = a[i]
  a[i] = a[i-1]
  a[i-1] = a1
 
print(*a)

# Правильное решение
a = [int(s) for s in input().split()]

# обратите внимание на множественное присваивание:
# справа от "=" стоит список из двух элементов,
# а слева -- две переменные,
# поэтому так делать можно
k, C = [int(s) for s in input().split()]

a.append(0)
for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = C
print(' '.join([str(i) for i in a]))
