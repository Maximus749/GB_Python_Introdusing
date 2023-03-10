# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод: ноутбук
# Вывод: 12


word = input("Input your word: ").upper()
count = 0
for i in word:
    if i in ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']:
        count += 1
    elif i in ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']:
        count += 2
    elif i in ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']:
        count += 3
    elif i in ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']:
        count += 4
    elif i in ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']:
        count += 5
    elif i in ['J', 'X', 'Ш', 'Э', 'Ю'] :
        count += 8
    elif i in ['Q', 'Z', 'Ф', 'Щ', 'Ъ']:
        count += 10
print(f"Вы заработали {count} очков")
