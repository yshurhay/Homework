# палиндром для слова
def task_1_word(word):
    return 'palindrome' if word.lower() == word[::-1].lower() else 'not palindrome'


# палиндром для предложения
def task_1_str(string):
    string = ''.join(char for char in string.lower() if char.isalpha())
    return task_1_word(string)


def task_2(dct1, dct2):
    dct1.update(dct2)
    return dct1


def task_3(num):
    return f'Да, это число {num}' if str(num)[0] == str(num)[1] else 'Нет'


def task_4(string):
    return bool(string)


def task_5(year):
    return 'високосный' if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else 'не високосный'


def task_6(a, b, c):
    sides = (a, b, c)
    max_side = max(sides)
    return 'можно' if max_side < sum(sides) - max_side else 'нельзя'


# print(task_1_word(input('Введите слово: ')))
# print(task_1_word('AdsgGsDa'))
# print(task_1_word(input('Введите предложение: ')))
# print(task_1_str('А роза упала на лапу Азора'))
# print(task_2({'a': 300, 'b': 400}, {'c': 500, 'd': 600}))
# print(task_3('22'))
# print(task_4(input()))
# print(task_5(2024))
# print(task_6(11, 22, 33))
