from random import choice, randint

NAMES = ['Alex', 'John', 'Olga', 'Maria', 'Artem']


def task_1(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} -> {value}')


def my_func_1():
    print('In_my_func_1')

    def my_func_2():
        print('In_my_func_2')

        def my_func_3():
            print('In_my_func_3')

            def my_func_4():
                print('In_my_func_4')

                def my_func_5():
                    print('In_my_func_5')

                return my_func_5()

            return my_func_4()

        return my_func_3()

    return my_func_2()


def generate_pupils(count):
    pupils_list = []

    for _ in range(count):
        pupil = {'name': choice(NAMES), 'age': randint(6, 18), 'marks': [randint(1, 10) for _ in range(5)]}
        pupils_list.append(pupil)

    return pupils_list


def sort_by_age(pupils):
    return sorted(pupils, key=lambda x: x['age'])


def tree_sum(numbers):
    num_list = []

    def root_sum(lst):
        for num in lst:
            if isinstance(num, int):
                num_list.append(num)
            else:
                root_sum(num)

    root_sum(numbers)
    return sum(num_list)

