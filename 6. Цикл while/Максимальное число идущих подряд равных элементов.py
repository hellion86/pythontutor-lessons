'''
Условие
Дана последовательность натуральных чисел, завершающаяся числом 0. Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу. 
'''

# Мое решение
s = 1
s1 = int(input())
count = 0
max = 0
while s != 0:
    s = int(input())
    if s == s1:
        count = count + 1
        if count > max:
            max = count
    else:
        count = 0
    s1 = s

print(max+1)

#Правильный вариант
prev = -1
curr_rep_len = 0
max_rep_len = 0
element = int(input())
while element != 0:
    if prev == element:
        curr_rep_len += 1
    else:
        prev = element
        max_rep_len = max(max_rep_len, curr_rep_len)
        curr_rep_len = 1
    element = int(input())
max_rep_len = max(max_rep_len, curr_rep_len)
print(max_rep_len)