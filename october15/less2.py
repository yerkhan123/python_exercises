"""
Задача 2. «Банкомат»
(while, if/elif/else, list, функции, try/except, f-strings)

Сделай мини-банкомат с меню.
Что делает:
Начальный баланс — 1000.
История операций — пустой список.
В цикле while True показать меню:

1 — пополнить
2 — снять
3 — история
4 — выход

Ввод обработать через try/except (если не число → сообщение об ошибке).

Логика:
пополнение → прибавить к балансу, добавить в историю "+500"
снятие → если хватает денег, вычесть; если нет → «Недостаточно средств»
история → вывести все операции через for
выход → break

После выхода — вывести итоговый баланс и количество операций (через len).

"""


balance = 1000
history = []

while True:
    print("\n=== БАНКОМАТ ===")
    print("1 — Пополнить")
    print("2 — Снять")
    print("3 — История")
    print("4 — Выход")

    try:
        choice = int(input("Выберите действие: "))
    except ValueError:
        print("Ошибка: введите число")
        continue

    if choice == 1:
        try:
            amount = int(input("Сумма пополнения: "))
        except ValueError:
            print("Ошибка: введите число")
            continue

        if amount > 0:
            balance += amount
            history.append(f"+{amount}")
            print(f"Баланс: {balance}")
        else:
            print("Сумма должна быть больше 0")

    elif choice == 2:
        try:
            amount = int(input("Сумма снятие: "))
        except ValueError:
            print("Ошибка: введите число")
            continue

        if amount <= 0:
            print("Сумма должна быть больше 0")
        elif amount <= balance:
            balance -= amount
            history.append(f"-{amount}")
            print(f"Баланс: {balance}")
        else:
            print("Недостаточно средств")

    elif choice == 3:
        print("=== ИСТОРИЯ ===")
        for operation in history:
            print(operation)

    elif choice == 4:
        print("Выход из банкомата")
        break

    else:
        print("Неверный пункт меню")

print(f"Итоговый баланс: {balance}")
print(f"Количество операций: {len(history)}")
