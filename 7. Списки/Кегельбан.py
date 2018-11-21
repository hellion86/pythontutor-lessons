'''
Условие
N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N. Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от li до ri включительно. Определите, какие кегли остались стоять на месте.
Программа получает на вход количество кеглей N и количество бросков K. Далее идет K пар чисел li, ri, при этом 1≤ li≤ ri≤ N.

Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.
'''

#Мое решение
N, K = [int(s) for s in input().split()]

keg = []
for i in range(N):
    keg.append('I')

l = []
r = []
for i in range(K):
    li,ri =[int(w) for w in input().split()]
    for j in range(li-1,ri):
        keg[j] = '.'

print (''.join(keg))

#Правильное решение
n, k = [int(s) for s in input().split()]
bahn = ['I'] * n
for i in range(k):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        bahn[j] = '.'
print(''.join(bahn))
