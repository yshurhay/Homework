import random, time


def task_1(number):
    for num in str(number):
        if not 0 <= int(num) <= 5:
            return 'not special'
    return 'special'


def task_2(string):
    return len(list(filter(counting, string.split())))


def counting(word):
    count = 0
    for letter in word:
        if letter in 'aeiou':
            count += 1
    return count > 3


def task_3():
    password = ''
    for _ in range(random.randint(8, 15)):
        choice = random.randint(1, 3)
        match choice:
            case 1:
                password += chr(random.randint(48, 57))
            case 2:
                password += chr(random.randint(65, 90))
            case 3:
                password += chr(random.randint(97, 122))

    return password


def generate_dict():
    names = ['Alex', 'John', 'Oleg']
    numbers = ['+123', '+321', '+567']
    contacts = []
    for _ in range(3):
        name = random.choice(names)
        number = random.choice(numbers)
        contacts.append({'name': name, 'number': number})
        names.remove(name)
        numbers.remove(number)

    return contacts


def calling(name, number):
    print(f'{name}: {number}')
    text = 'Идёт вызов'
    print(text, end='')
    for _ in range(3):
        time.sleep(1)
        print('.', end='')


def try_to_calling(contacts, name='', number=''):
    for contact in contacts:
        if name == contact['name'] or number == contact['number']:
            return calling(contact['name'], contact['number'])
    return 'Такого контакта нет'


