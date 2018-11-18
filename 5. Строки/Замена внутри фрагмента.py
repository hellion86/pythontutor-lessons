'''
Условие

Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения. 
'''
s = input()
 

s1 = list(s[s.find('h')+1:s.rfind('h')])

for i in range(len(s1)):
    if s1[i] == 'h':
        s1[i] = s1[i].upper()
print(s[:s.find('h')+1]+''.join(s1)+s[s.rfind('h'):])
