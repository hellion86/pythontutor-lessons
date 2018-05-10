'''
Условие
Определите количество четных элементов в последовательности, завершающейся числом 0. 

'''
# Мое решение 
s = 1
count = 0
while s != 0:
    s = int(input())
    if s % 2 == 0:
        count = count + 1
            
print(count-1)

# Правильное решение

num_even = -1
element = -1
while element != 0:
    element = int(input())
    if element % 2 == 0:
        num_even += 1
print(num_even)
