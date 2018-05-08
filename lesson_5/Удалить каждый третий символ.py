'''
Условие

Дана строка. Удалите из нее все символы, чьи индексы делятся на 3. 
'''

s = input()
s1 = list(s)
for i in range(len(s1)):
    if i % 3 == 0:
        s=s.replace(s1[i],' ',1)
print(s.replace(' ',''))
