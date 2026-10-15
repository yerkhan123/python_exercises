"""
Задача: Пиццерия
----------------------------------------------------

Даны входные данные (вы можете скопировать этот текст в исходный код)

item1_name  = "Маргарита"
item1_price = 2200
item1_qty   = 2

item2_name  = "Пепперони"
item2_price = 2700
item2_qty   = 1

item3_name  = "Кола 1л"
item3_price = 700
item3_qty   = 3

item4_name  = "Чизкейк"
item4_price = 1500
item4_qty   = 2

delivery         = True
delivery_price   = 800
discount_percent = 10

Требуется:------------------------------------------
Для каждой позиции посчитать price * qty
Найти подытог (сумма всех позиций)
Посчитать скидку от подытога
Посчитать итог со скидкой
Учесть доставку через bool -> int(True) = 1, int(False) = 0
Найти среднюю стоимость позиции. средняя_стоимость_позиции = подытог / количество_позиций
Вывести чек с ровным выравниванием (используйте те знанния которые прошли на уроках)

Формулы:-------------------------------------------
1. Подытог       = сумма всех позиций (price * qty)
2. Скидка        = подытог * discount_percent / 100
3. Итог со скидкой = подытог − скидка
4. Доставка      = delivery_price * int(delivery)
5. К ОПЛАТЕ      = итог со скидкой + доставка

----------------------------------------------------
Пример результата, который необходимо получить:

========== ЧЕК ==========
Маргарита     2 x 2200 = 4400
Пепперони     1 x 2700 = 2700
Кола 1л       3 x  700 = 2100
Чизкейк       2 x 1500 = 3000
-------------------------
Подытог:              12200
Скидка (10%):          1220
Итог со скидкой:      10980
Доставка:               800
-------------------------
К ОПЛАТЕ:             11780
=========================
Позиций: 4
Средняя стоимость позиции: 3050.0
"""

item1_name = "Маргарита"
item1_price = 2200
item1_qty = 2

item2_name = "Пепперони"
item2_price = 2700
item2_qty = 1

item3_name = "Кола 1л"
item3_price = 700
item3_qty = 3

item4_name = "Чизкейк"
item4_price = 1500
item4_qty = 2

delivery = True
delivery_price = 800
discount_percent = 10

# Стоимость каждой позиции
total1 = item1_price * item1_qty
total2 = item2_price * item2_qty
total3 = item3_price * item3_qty
total4 = item4_price * item4_qty

# Подытог
subtotal = total1 + total2 + total3 + total4

# Скидка
discount = subtotal * discount_percent / 100

# Итог со скидкой
after_discount = subtotal - discount

# Доставка
delivery_total = delivery_price * int(delivery)

# К оплате
final_total = after_discount + delivery_total

# Количество позиций
count = 4

# Средняя стоимость позиции
average = subtotal / count

# Чек
print("========== ЧЕК ==========")
print(f"{item1_name:<12} {item1_qty} x {item1_price:4} = {total1}")
print(f"{item2_name:<12} {item2_qty} x {item2_price:4} = {total2}")
print(f"{item3_name:<12} {item3_qty} x {item3_price:4} = {total3}")
print(f"{item4_name:<12} {item4_qty} x {item4_price:4} = {total4}")
print("-------------------------")
print(f"{'Подытог:':<20}{subtotal:>5}")
print(f"{'Скидка (10%):':<20}{discount:>5.0f}")
print(f"{'Итог со скидкой:':<20}{after_discount:>5.0f}")
print(f"{'Доставка:':<20}{delivery_total:>5}")
print("-------------------------")
print(f"{'К ОПЛАТЕ:':<20}{final_total:>5.0f}")
print("=========================")
print(f"Позиций: {count}")
print(f"Средняя стоимость позиции: {average}")
