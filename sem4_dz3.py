"""
Возьмите задачу о банкомате из семинара 2.
Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.

Напишите программу банкомат. Начальная сумма равна нулю.
Допустимые действия: пополнить, снять, выйти.
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие - 1,5% от суммы снятия,
но не менее 30 и не более 600 у.е.
После каждой третьей операции пополнения или снятия
начисляются проценты - 3%.
Нельзя снять больше чем на счете.
При превышении суммы в 5 млн., вычитать налог на богатство 10%
перед каждой операцией, даже ошибочной.
Любое действие выводит сумму денег.
"""
from decimal import Decimal

min_sum = 50
comm_percent = Decimal(0.015)
min_comm = 30
max_comm = 600
bonus = Decimal(0.03)
rich_limit = 5_000_000
rich_tax = Decimal(0.1)


def get_money(balance: Decimal):
    print('Комиссия за снятие -1,5%')
    g_money = Decimal(input('Введите сумму снятия: '))
    prcnt = g_money * comm_percent
    if prcnt < min_comm:
        prcnt = min_comm
    elif prcnt > max_comm:
        prcnt = max_comm

    if g_money % min_sum == 0:
        g_money = g_money - prcnt
        if g_money <= balance:
            return balance - g_money
        else:
            print('Недостаточно средств на счете!')
            return balance
    else:
        while True:
            print('Сумма снятия должна быть кратна 50')
            g_money = Decimal(input('Введите сумму снятия: '))
            if g_money % min_sum == 0:
                g_money = g_money - prcnt
                if g_money <= balance:
                    return balance - g_money
                else:
                    print('Недостаточно средств на счете!')
                    return balance
            break
        return balance - g_money


def put_money(balance: Decimal):
    p_money = Decimal(input('Введите сумму пополнения: '))
    if p_money % min_sum == 0:
        balance = balance + p_money
        return balance

    else:
        while True:
            print('Сумма пополнения должна быть кратная 50!')
            p_money = Decimal(input('Введите сумму пополнения: '))
            if p_money % min_sum == 0:
                break
        balance = balance + p_money
        return balance


def menu(balance: Decimal, count: int):
    if balance > rich_limit:
        print('C баланса счета свыше 5млн, удерживается налог на богатство -10%!!!')
        balance *= (1 - rich_tax)

    print(f'Баланс счета: {balance:.2f}')
    menu_dct = {'1': 'Снять',
                '2': 'Пополнить',
                '3': 'Выход'}
    for k, v in menu_dct.items():
        if k.isdigit():
            print(f'{k}: {v}')
        else:
            print(v)

    choice = input('Выберите пукт меню: ')
    if choice == '3':
        print(f'Баланс счета: {balance:.2f}')
        print('До встречи!')
        exit()
    elif choice == '1':
        balance = get_money(balance)
        count += 1
        if count % 3 == 0:
            print('За 3-ю операцию вам начислен бонус 3%')
            balance *= (1 + bonus)
        menu(balance, count)
    elif choice == '2':
        balance = put_money(balance)
        count += 1
        if count % 3 == 0:
            print('За 3-ю операцию вам начислен бонус 3%')
            balance *= (1 + bonus)
        menu(balance, count)
    else:
        print('Неверная команда!')
        menu(balance, count)
    return balance, count


if __name__ == '__main__':
    print('Добро пожаловать в Банкомат')
    balance = 0
    count = 0
    menu(balance, count)
