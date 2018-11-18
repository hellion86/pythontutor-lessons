'''
Условие

По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N. Выведите показатель степени и саму степень.

Операцией возведения в степень пользоваться нельзя!
'''

#Мое решение
i = int(input())
sum = 1
count = 0
while (sum * 2) <= i:
    sum =  sum * 2
    count = count + 1 
 
print(count,sum)

#Правильное
n = int(input())
two_in_power = 2
power = 1
while two_in_power <= n:
    two_in_power *= 2
    power += 1
print(power - 1, two_in_power // 2)