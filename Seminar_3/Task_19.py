# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]

# РЕШЕНИЕ
# spisok = [1, 2, 3, 4, 5, 0, -7, 99]
# k = 4
# for i in range (k):
#     a = spisok.pop(-1)
#     spisok.insert(0,a) 
# print(spisok)

array = input().split(",") 
k = int(input())
for _ in range(k):
	array.insert(0, array.pop()) 
print(*array)