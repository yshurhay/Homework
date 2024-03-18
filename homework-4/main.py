def task_1(string):
    vowel_letters = 'АЕЁИОУЫЭЮЯ'
    count = 0
    for letter in string.upper():
        if letter in vowel_letters:
            count += 1

    return count


def task_2(string):
    count = 0
    for letter in string.lower():
        if letter == 'a':
            count += 1

    return count


def task_3(num1, num2):
    result = 1
    factor = 2

    while num1 != 1 or num2 != 1:

        if num1 % factor == 0 and num2 % factor == 0:
            result *= factor
            num1 //= factor
            num2 //= factor

        elif num1 % factor == 0:
            result *= factor
            num1 //= factor

        elif num2 % factor == 0:
            result *= factor
            num2 //= factor

        else:
            factor += 1

    return result


def task_4():
    num = input('num: ')
    while num != 'exit':

        if num.isalpha():
            num = input('num: ')
            continue

        flag = True
        num = int(num)
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break

        if flag:
            print(f'\nNumber {num} is prime\n')
        else:
            print(f'\nNumber {num} is not prime\n')

        num = input('num: ')


def task_5(string):
    return ' '.join(f'{ord(letter) - 96}' for letter in string.lower() if letter.isalpha())


