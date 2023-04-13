# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

A = int(input("Ведите искомый номер числа фибоначчи "))     

if A == 0:
    print("0")

elif A == 1:
    print("1\nили")

if (A < 0):
    print("-1")
else:
    fib1 = 0
    fib2 = 1
    fib3 = 1
    FibIndx = 2

    while (fib2 < A):
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
        FibIndx += 1

    result = FibIndx

if fib2 == A:

    print(result)

else:
    print("-1")

    
# n = int(input("Введите число Фибоначчи: "))
# print((round((5*n*n+4)**0.5, 0)) == (5*n*n+4)**0.5 or (round((5*n*n-4)**0.5, 0)) == (5*n*n-4)**0.5)

# y = 1
# z = 2
# count = 4

# # while (((1+5**0.5)/2)**n-((1-5**0.5)/2)**n)/(5**0.5) < n

# while z!=n:
#     temp = z
#     z = z+y
#     y = temp
#     count+=1

# print(count)