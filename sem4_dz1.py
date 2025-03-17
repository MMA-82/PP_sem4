"""
Напишите функцию для транспонирования матрицы
"""
from random import randint


def transp_matrix(matrix: list[list]) -> list[list]:
    """
    Транспонирует матрицу
    """
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix))]


if __name__ == '__main__':
    x = int(input("Введите количество столбцов: "))
    y = int(input("Введите количество строк: "))
    while x != y:
        print('Размеры должны быть равны, попробуй еще!!!')
        x = int(input("Введите количество столбцов: "))
        y = int(input("Введите количество строк: "))
        # continue
    else:
        print('Задана матрица:')
        matrix = [[randint(1, 9) for i in range(x)] for j in range(y)]
        for _ in matrix:
            print(_)
        print()
        print('Получаем транспонированную матрицу:')
        for _ in transp_matrix(matrix):
            print(_)
