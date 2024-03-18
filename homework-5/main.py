def task_1(array):
    return [num ** 2 for num in array]


def task_2(strings):
    return [string for string in strings if len(string) > 5]


def task_3(array):
    return [num for num in array if num % 2 == 0]


def task_4(array):
    result = 0
    for num in array:
        if num % 2 == 0:
            result += num ** 2

    return result


def task_5(strings):
    return [string for string in strings if string[0] == 'b']


def task_6(array):
    return [num for num in array if 10 < num < 20]


def task_7(array):
    for num in array:
        if num <= 0:
            return False

    return True


def task_8(strings):
    return [string for string in strings if string.isdigit()]
