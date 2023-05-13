# Задача No35. Решение в группах
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5 Output: yes

n = int(input("Введите число: "))

def prime(x, div = 2):
    if x % div == 0:
        return False
    elif x == div:
        return True
    return prime(x, div+1)

print()