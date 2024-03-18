from random import choice


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def number_guess(secret_number: str):
    if not secret_number.isdigit():
        return ValueError('You must input an integer')
    if not 0 <= int(secret_number) <= 100:
        return Exception('Your number must be in range 100')

    try:
        secret_number = int(secret_number)
        array = [x for x in range(101)]

        for _ in range(7):
            try_number = choice(array)
            print(f'Bot try number: {try_number}')

            if try_number == secret_number:
                return 'Bot won!'
            else:
                question = choice(('lower', 'greater'))
                print(f'Is your number {question} than that?')
                answer = input('Input y/n: ')
                print()

                match (question, answer):
                    case ('lower', 'y') | ('greater', 'n'):
                        array = array[:array.index(try_number)]
                    case ('lower', 'n') | ('greater', 'y'):
                        array = array[array.index(try_number) + 1:]
                    case _:
                        return 'Not correct input'

        else:
            return 'Attempts are over. Bot lose!'
    except Exception:
        return ValueError('Error in the game')


print(number_guess(input('Input your number: ')))

