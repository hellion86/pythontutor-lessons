'''
Условие
Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φn = A. Если А не является числом Фибоначчи, выведите число -1. 
'''
#Мое решение
r = int(input())
s1 = 1
s2 = 1
sum = 0
i = 2
count = -1
while sum <= r:
    sum = s1 + s2
    s1 = s2
    s2 = sum
    i = i + 1
    if sum == r:
        count = i
print(count)

#Правильный вариант
a = int(input())
if a == 0:
    print(0)
else:
    fib_prev, fib_next = 0, 1
    n = 1
    while fib_next <= a:
        if fib_next == a:
            print(n)
            break
        fib_prev, fib_next = fib_next, fib_prev + fib_next
        n += 1
    else:
        print(-1)