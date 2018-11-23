'''
Условие
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. В этой задаче нельзя использовать циклы — используйте рекурсию.
'''

# Мое решение 
n = int(input())
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibo(n-1) + fibo(n-2)
       
print(fibo(n))

# Правильное решение
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(int(input())))