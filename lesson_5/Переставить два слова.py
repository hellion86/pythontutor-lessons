'''
Условие

Дана строка, состоящая ровно из двух слов, разделенных пробелом. Переставьте эти слова местами. Результат запишите в строку и выведите получившуюся строку.

При решении этой задачи не стоит пользоваться циклами и инструкцией if. 
'''
s = input()
print(s[s.find(' '):] +' '+ s[:s.find(' ')])