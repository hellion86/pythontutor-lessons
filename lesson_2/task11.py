'''Условие
Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали, или наоборот. Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую одним ходом.
'''

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
    print('YES')
else:
    print('NO')