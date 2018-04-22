'''Условие
Яша плавал в бассейне размером N × M метров и устал. В этот момент он обнаружил, что находится на расстоянии x метров от одного из длинных бортиков (не обязательно от ближайшего) и y метров от одного из коротких бортиков. Какое минимальное расстояние должен проплыть Яша, чтобы выбраться из бассейна на бортик? Программа получает на вход числа N, M, x, y. Программа должна вывести число метров, которое нужно проплыть Яше до бортика.
'''
n = int(input())
m = int(input())
x = int(input())
y = int(input())

if n < m:
    print(min(abs(n - x),abs(m - y),x,y))
else:
    print(min(abs(m - x),abs(n - y),x,y))