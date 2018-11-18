'''
Условие
Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы! 
'''

# Мое решение 
a = input().split()
for i in  a:
   if int(i) % 2 == 0:
       print(i)

# Правильное решение
s=input()
a=[int(s) for s in s.split()]
for i in a:
    if int(i)%2 == 0:
       print(i, end=' ')