'''
Условие
Дан текст: в первой строке записано число строк, далее идут сами строки. Определите, сколько различных слов содержится в этом тексте.

Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
'''

#Мое решение
n = int(input())
text = []
for i in range(n):
    text.append(input().split())

b = [x for xs in text for x in xs]
s = set(b)
count = 0  
for j in s:
     count = count + 1

print(count)

#Правильное решение
words = set()
for _ in range(int(input())):
    words.update(input().split())
print(len(words))