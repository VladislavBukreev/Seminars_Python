# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# Решение 1:

strl = "a a a b c a a d c d d"

a = strl.split()
b = dict().fromkeys(a,0)
print(b)

for i in a:
    if b[i] == 0:
        print(i, end = " ")
    else:
        print(f'{i}_{b[i]}', end = '')

# Решение 2:

# stroka = input().split()
# result = {}
# for i in stroka:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     result[i] = result.get(i, 0) + 1


# СУПЕРРЕШЕНИЕ
# string = "a a a b c a a d c d d".split()

# for i in range(len(string)):
#     print(f"{string[i]}_{string[0:i].count(string[i])}" if string[0:i].count(string[i]) != 0 else string[i], end=" ")

