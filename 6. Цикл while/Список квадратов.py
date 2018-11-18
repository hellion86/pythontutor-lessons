'''
Условие
По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания. 
'''
'''
i = int(input())
sum = 0
s = 0
while sum < i: 
    s = s + 1
    sum = s ** 2
    if sum > i:
        break
    print(sum)
'''

n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1