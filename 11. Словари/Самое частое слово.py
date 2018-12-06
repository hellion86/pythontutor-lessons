'''
Условие
Дан текст: в первой строке задано число строк, далее идут сами строки. 
Выведите слово, которое в этом тексте встречается чаще всего. 
Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
'''

#Мое решение
s = {}
 
for i in range(int(input())):
    a = input().split()
    for j in range(len(a)):
        if a[j] in s:
            s[a[j]] = s[a[j]] + 1
        else:
            s[a[j]] = 0
l = -1
for k,v in s.items():
    if l < v:
        l = v
        item = k
    elif l == v:
        s = item
        if s < k:
            item = s
        else:
            item = k
print(item)


#Правильное решение
counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1
        
max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))