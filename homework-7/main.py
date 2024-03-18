def task_1(string):
    symbols = ',.:;!?#'
    text = ''.join(char for char in string if char not in symbols)
    words = text.split()
    min_len = len(min(words))

    return list(filter(lambda word: len(word) == min_len, words))


def isarmstrong(num):
    result = 0
    for dig in str(num):
        result += int(dig) ** len(str(num))

    return True if result == num else False
