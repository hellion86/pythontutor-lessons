'''
Условие
Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте количество нулей среди введенных чисел и выведите это количество. Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.
'''

s = int(input())
count = 0
for i in range(0,s):
    m = int(input())
    if m == 0:
        count += 1
print(count)
