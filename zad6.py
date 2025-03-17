"""
Функция получает на вход список чисел и два индекса.
Вернуть сумму чисел между переданными индексами.
Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""
from random import randint


def sum_range(numbers: list, x1: int, x2: int) -> int:
    """
    Возвращает сумму чисел в промежутке между индексами. 
    """
    if x1 > x2:
        x1, x2 = x2, x1
    if x1 < 0:
        x1 = 0
    if x2 >= len(numbers):
        x2 = len(numbers) - 1
    return sum(numbers[x1:x2+1])


if __name__ == '__main__':
    numbers = [randint(0, 10) for i in range(10)]
    print('Есть список чисел: ', *numbers)
    x1 = int(input('Введите первый индекс (от 0 до 9): '))
    x2 = int(input('Введите второй индекс (от 0 до 9): '))
    print(f'Сумма чисел между индексами: {sum_range(numbers, x1, x2)}')
