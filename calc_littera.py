#подсчет числа имени, фамилии или любого слова на английском или русском языках

eng_alphabet = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9,
    "j": 1, "k": 2, "l": 3, "m": 4, "n": 5, "o": 6, "p": 7, "q": 8, "r": 9,
    "s": 1, "t": 2, "u": 3, "v": 4, "w": 5, "x": 6, "y": 7, "z": 8, " ": 0
}

rus_alphabet = {
    "а": 1, "б": 2, "в": 3, "г": 4, "д": 5, "е": 6, "ё": 7, "ж": 8, "з": 9,
    "и": 1, "й": 2, "к": 3, "л": 4, "м": 5, "н": 6, "о": 7, "п": 8, "р": 9,
    "с": 1, "т": 2, "у": 3, "ф": 4, "х": 5, "ц": 6, "ч": 7, "ш": 8, "щ": 9,
    "ъ": 1, "ы": 2, "ь": 3, "э": 4, "ю": 5, "я": 6, " ": 0
}

#сложение цифр в числах
def sum_digit(numeral):
    print("Полная сумма: ", numeral)
    result = 0
    while numeral > 0:
        result += numeral % 10
        numeral = numeral // 10
    return result

#считаем число слова в английском алфавите
def count_letters_eng(word):
    item = word.lower()
    count = 0
    for i in item:
        count = count + eng_alphabet[i]
    if count <= 11:
        return count
    else:
        return sum_digit(count)

#считаем число слова в русском алфавите
def count_letters_rus(word):
    item = word.lower()
    count = 0
    for i in item:
        count = count + rus_alphabet[i]
    if count <= 11:
        return count
    else:
        return sum_digit(count)

while True:
    answer = input("На каком языке вводим слова? eng/рус ")
    if answer == 'eng':
        word1 = input("Введите слово на английском: ")
        print("Число вашего слова: ", count_letters_eng(word1))
    elif answer == 'рус':
        word1 = input("Введите слово на русском: ")
        print("Число вашего слова: ", count_letters_rus(word1))
    else:
        print("Неверный ввод!")
    answer2 = input("Хотите еще? 1/0: ")
    if answer2 == '1':
        True
    else:
        break