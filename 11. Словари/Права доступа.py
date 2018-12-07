'''
Условие
Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.

Для слова из словаря, записанного в последней строке, определите его синоним.
'''

#Мое решение
n = int(input())
slov = {}
for i in range(n):
    s,b = input().split()
    slov[s] = b
answ = input()

for key,value in slov.items():
    if answ == key:
        print(value)
    elif answ == value:
        print(key)


#Правильное решение
n = int(input())
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])