import random


def task_1(list_1: list, list_2: list) -> list:
    return [list_1[i] + list_2[i] for i in range(len(list_1))]


def is_palindrome(num: str) -> bool:
    return num == num[::-1]


def task_2(number: int) -> int:
    number += 1
    while not is_palindrome(str(number)):
        number += 1
    return number


def task_3(string: str) -> str:
    lst = string.split()
    digits = '0123456789'
    result = []
    for i in digits:
        for word in lst:
            if i in word:
                result.append(word)

    return ' '.join(word for word in result)


def create_list(numbers_count: int) -> list:
    return [random.randint(1, 5) for _ in range(numbers_count)]


def counting(array_list: list) -> int:
    array_set = set(array_list)
    count = 0
    for num in array_set:
        if array_list.count(num) > 1:
            count += 1
    return count


def task_4(numbers_count: int) -> int:
    array_list = create_list(numbers_count)
    print(array_list)
    return counting(array_list)


def task_5(words: list, substr: str) -> list:
    return [word for word in words if word.lower().startswith(substr.lower())]


def task_6(number: int) -> bool:
    for num in range(2, number):
        if number % num == 0:
            return False
    return True




