'''
Условие
Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности больше предыдущего элемента. 
'''

# Мое решение

s = 1
s1 = int(input())
count = 0

while s != 0:
    s = int(input())
    if s > s1:
        count = count + 1
    s1 = s
    
print(count)
# Правильное решение
prev = int(input())
answer = 0
while prev != 0:
    next = int(input())
    if next != 0 and prev < next:
        answer += 1
    prev = next
print(answer)