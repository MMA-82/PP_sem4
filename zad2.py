"""
Напишите функцию, которая принимает строку текста.
Сформируйте список с уникальными кодами Unicode 
каждого символа строки, отсортированный по убыванию.
"""


def text_unicode(text: str) -> list:
    """
    Возвращает список с уникальными кодами Unicode.
    """
    return list(map(ord, sorted(set(text), reverse=True)))


if __name__ == '__main__':
    print(text_unicode(input('Введите строку: ')))
