﻿'''
Условие
С начала суток часовая стрелка повернулась на угол в α градусов. Определите сколько полных часов, минут и секунд прошло с начала суток, то есть решите задачу, обратную задаче «Часы - 1». Запишите ответ в три переменные и выведите их на экран.
'''

a = float(input())

print ( a * 120 // 3600, a * 120 % 3600 //60, int(a * 120 %3600 %60))