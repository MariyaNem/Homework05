# Дана строка(возможно пустая),состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения:
# Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.

def num_of_simbols(list):
    result = ''
    prev_char = ''
    count = 1
    if not list: return ''
    for char in list:
        if char != prev_char:
            if prev_char:
                result += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        result += str(count) + prev_char
        return result

input_list = str(input("Введите строку: "))
print(input_list)
x = num_of_simbols(input_list)
print(x)