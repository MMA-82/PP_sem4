"""
Функция получает на вход список чисел.
Отсортируйте его элементы in place без использования 
встроенных в язык сортировок.
Как вариант, напишите сортировку пузырьком.
Ее описание есть в википедии.
"""


def sort_numbers(lst: list) -> None:
    """
    Сортирует на месте.
    """
    for _ in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(*lst)


if __name__ == '__main__':
    # lst = [int(i) for i in input('Введите числа: ').split()]
    # sort_numbers(lst)
    # print(*lst)
    sort_numbers([int(i) for i in input('Введите числа: ').split()])
