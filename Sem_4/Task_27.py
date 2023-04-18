# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов.
# Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# РЕШЕНИЕ 1

# x = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# y = x.replace(".",' ').split(' ')
# newSecondList = []


# for i in y: 
#     if i not in newSecondList:
#         newSecondList.append(i)
# print(len(set(y)))



# РЕШЕНИЕ 3:

someText = """She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"""
someList = someText.lower().replace(".", " ").split(" ")
print(len(set(someList)))

newSecondList = []
for i in someList: 
    if i not in newSecondList:
        newSecondList.append(i)
print(len(newSecondList))

# РЕШЕНИЕ 2

# text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".split()
# set_result = set()
# for i in text:
#     set_result.add(i.lower())
# print(len(set_result))