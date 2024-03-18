# 1 задание
a = input('Введите первое число: ')
b = input('Введите второе число: ')
print('Значения до:')
print(f'a: {a}')
print(f'b: {b}')

a, b = b, a
print('Значения после:')
print(f'a: {a}')
print(f'b: {b}')

# 2 задание
side = float(input('Введите сторону квадрата: '))

diagonal = side * (2 ** 0.5)
square = side ** 2
perimetr = side * 4

print(f'Диагональ: {round(diagonal, 1)}')
print(f'Площадь: {round(square, 1)}')
print(f'Периметр: {round(perimetr, 1)}')

# 3 задание

# 1 способ
num = int(input('Введите число: '))
result = num + (num * 10 + num) + (num * 100 + num * 10 + num)
print(f'n + nn + nnn = {result}')

# 2 способ
num = input('Введите число: ')
result = int(num * 3) + int(num * 2) + int(num)
print(f'n + nn + nnn = {result}')