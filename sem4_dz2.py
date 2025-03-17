"""
Напишите функцию принимающую на вход только ключевые параметры
и возвращающую словарь, где ключ — значение переданного аргумента,
а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.
"""
# def inv_dict(vals: int, names: str) -> dict:


def inv_dict(**kwargs) -> dict:
    """
    Возвращает словарь, в котором значения аргументов - ключи,
    а значения - названия аргументов.
    """
    return {v if v.__hash__ is not None else str(v): k for k, v in kwargs.items()}


if __name__ == '__main__':
    print(inv_dict(arg1=1, arg2=2))
    print(inv_dict(arg1=1, arg2=[1, 2, 3, 4, 5]))
    print(inv_dict(arg1='Name', arg2=2, arg3=2.5, arg4=[1, 2, 3, 4, 5]))
