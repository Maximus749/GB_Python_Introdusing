# Задача №27. Решение в группах
# Пользователь вводит текст(строка).
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов.
# Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So " \
       "if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# text = "She sells sea shells on the sea shore;The shells that she sells are sea shells " \
#        "I'm sure.So if she sells sea shells on the sea shore,I'm sure that the shells are sea shore shells."
text1 = text.lower().split()
# print(text1)
text2 = set(text1)
print(len(text2))
