'''
Условие
По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.
'''

n = int(input())
s = ''
for i in range(n):
    i += 1
    s = s + str(i)
    print(s)
