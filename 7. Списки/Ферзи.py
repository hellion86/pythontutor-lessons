'''
Условие
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
'''

# Мое первоночальное решение, в один цикл, не заработало, не попедил конец листа, не смог разобрать как правильно итерироваться:
a = []

for s in range(8):
    a.append(input().split())

count = 0
for i in range(8):
	if abs( int(a[i][0]) - int(a[i+1][0]) ) == abs( int(a[i][1]) - int(a[i+1][1]) ) or (a[i][0] == a[i+1][0]) or (a[i][1] == a[i+1][1]):
    	count = count + 1        

if count > 0:
	print("YES")
else:
	print("NO")

# Психанул и подсмотрел у других:
a = []
b = []
for s in range(8):
    x, y = [int(s) for s in input().split()]
    a.append(x)
    b.append(y)
count = 0
for i in range(8):
    for j in range( i + 1, 8):
        if a[i] == a[j] or b[i] == b[j] or abs(a[i] - a[j]) == abs(b[i] - b[j]):
            count = count + 1

if count > 0:
	print("YES")
else:
	print("NO")

 

# Правильное решение
n = 8
x = []
y = []
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)

correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False

if correct:
    print('NO')
else:
    print('YES')