# Задача No31.
# факториал

def factorial(n):
    if n == 1:
        return 1
    else: 
        return n * factorial(n-1)

f = int(input(" Введите число "))
print(f'Факториал числа - {factorial(f)}')


# Фибоначи

def fib(n):
    if n in[1,2]:
        return 1
    return fib (n-1) + fib(n-2)
    
f = int(input(" Введите число "))
print(f'фибоначи числа - {fib(f)}')

