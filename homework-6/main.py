
def match_task_1(letter):
    if len(letter) != 1:
        return 'error input'
    match letter.upper():
        case 'A' | 'E' | 'I' | 'O' | 'U' | 'Y':
            return 'vovel'
        case _:
            return 'consonant'


def match_task_2(day):
    match day.upper():
        case 'SATURDAY' | 'SUNDAY':
            return 'holiday'
        case 'MONDAY' | 'TUESDAY' | 'WEDNESDAY' | 'THURSDAY' | 'FRIDAY':
            return 'workday'
        case _:
            return 'error input'


def match_task_3(fruit):
    fruits = {
        'BANANA': 'YELLOW',
        'APPLE': 'RED',
        'ORANGE': 'ORANGE',
        'LEMON': 'YELLOW'
    }

    match fruit.upper():
        case 'BANANA' | 'APPLE' | 'ORANGE' | 'LEMON':
            return fruits[fruit.upper()]
        case _:
            return 'error input'


def match_task_4(mark):
    marks = {
        1: 'Very bad',
        2: 'Bad',
        3: 'Satisfactorily',
        4: 'Good',
        5: 'Great'
    }

    match mark:
        case 1 | 2 | 3 | 4 | 5:
            return marks[mark]
        case _:
            return 'error input'

