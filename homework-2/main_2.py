def first_task():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(list(set(a).intersection(set(b))))


def second_task():
    text = input('Input smth: ')
    if len(text) == len(set(text)):
        print('isogram')
    else:
        print('not isogram')

