'''
Условие
Напишите функцию capitalize(), которая принимает слово из маленьких латинских букв и возвращает его же, меняя первую букву на большую.
Например, print(capitalize('word')) должно печатать слово Word.

На вход подаётся строка, состоящая из слов, разделённых одним пробелом. Слова состоят из маленьких латинских букв. Напечатайте исходную строку, сделав так, чтобы каждое слово начиналось с большой буквы. При этом используйте вашу функцию capitalize().

Напомним, что в Питоне есть функция ord(), которая по символу возвращает его код в таблице ASCII, и функция chr(), которая по коду символа возвращает сам символ. Например, ord('a') == 97, chr(97) == 'a'.
'''

# Мое решение 
def capitalize(s):
    for i in range(len(s)):
        if i == 0:
            char = chr(int(ord(s[i])) - 32)
            s[i] = char
        if s[i] == ' ':
            char = chr(int(ord(s[i+1])) - 32)
            s[i+1] = char
    return ''.join(s)
    
j = list(input())

print(capitalize(j))


# Правильное решение
def capitalize(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]

source = input().split()
res = []
for word in source:
    res.append(capitalize(word))
print(' '.join(res))