from random import randint, choices


def task_1():
    for x in range(1, 11):
        yield x ** 2


def task_2(start, end):
    for x in range(start, end):
        if x % 2 == 0:
            yield x


def task_3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def task_4(start, end):
    while True:
        yield randint(start, end)


WORDS = ["Яблоко", "Машина", "Кот", "Дом", "Школа", "Книга", "Солнце", "Стол", "Вода", "Путешествие"]


def task_5():
    while True:
        yield ' '.join(choices(WORDS, k=randint(4, len(WORDS))))


def task_6():
    while True:
        r, g, b = (randint(-255, 255) for _ in range(3))
        yield r, g, b


def is_prime(number):
    for x in range(2, int(number ** 1/2) + 1):
        if number % x == 0:
            return False
    return True


def task_7(number):
    for x in range(number):
        if is_prime(x):
            yield x


def task_8(letters, length, attempt=''):
    if not length:
        yield attempt
    else:
        for letter in letters:
            yield from task_8(letters, length - 1, attempt + letter)


def task_9(numbers, length, attempt=''):
    numbers = str(numbers)
    if not length:
        yield attempt
    else:
        for number in numbers:
            yield from task_8(numbers, length - 1, attempt + number)


SYMBOLS = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()]'


def task_10(length):
    while True:
        yield ''.join(choices(SYMBOLS, k=length))

