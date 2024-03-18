def first_task():
    string = input('Input numbers: ')
    str_array = string.split(',')
    str_tuple = tuple(str_array)
    print(str_array)
    print(str_tuple)


def second_task():
    number = list(input('Input number: '))
    number.sort()
    print(f'Max number: {"".join(number[::-1])}')


def third_task():
    print(f"Max digit in number: {max(list(input('Input number: ')))}")


def fourth_task():
    arr = ['Alex', 'Mark', 'John', 'Max']
    if len(arr) == 0:
        print('no one likes this')
    elif len(arr) == 1:
        print(f'{arr[0]} likes this')
    elif len(arr) == 2:
        print(f'{arr[0]} and {arr[1]} like this')
    elif len(arr) == 3:
        print(f'{arr[0]}, {arr[1]} and {arr[2]} like this')
    else:
        print(f'{arr[0]}, {arr[1]} and {len(arr) - 2} others like this')

# def is_armstrong(num):
#     summ = 0
#     for i in num:
#         summ += int(i) ** len(num)
#
#     return summ == int(num)
#
#
# def find_nearest_armstrong(num):
#     left_num = int(num)
#     right_num = int(num)
#
#     while not is_armstrong(str(left_num)) and not is_armstrong(str(right_num)):
#         left_num -= 1
#         right_num += 1
#
#     if is_armstrong(str(left_num)):
#         return left_num
#     else:
#         return right_num
#
#
# number = input('Input number: ')
# print(f'The nearest Armstrong number is {find_nearest_armstrong(number)}')
