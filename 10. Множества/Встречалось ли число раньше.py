'''
Условие
Во входной строке записана последовательность чисел через пробел. 
Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.
'''

#Мое решение
m=[int(a) for a in input().split()]
s = set()

for i in  m:
    if s & {i}:
        print('YES')
    else:
        print('NO')
        s.add(i)


	
#Правильное решение
numbers = [int(s) for s in input().split()]
occur_before = set()
for num in numbers:
    if num in occur_before:
        print('YES')
    else:
        print('NO')
        occur_before.add(num)
