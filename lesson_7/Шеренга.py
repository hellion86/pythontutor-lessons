'''
Условие
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.

Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю. После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.

Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них. 
'''

# Мое решение 
a = [int(s) for s in input().split()]
rost = int(input())
for i in range(len(a)):
    if a[i] > rost and rost > a[i-1]:
        position = i+2
    else:
        position = len(a)+1
    if rost > a[i]:
        position = i+1
        break;
print(position)

# Правильное решение
a = [int(i) for i in input().split()]
x = int(input())
pos = 0
while pos < len(a) and a[pos] >= x:
    pos += 1
print(pos + 1)