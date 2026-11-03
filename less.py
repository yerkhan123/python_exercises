# # list — хранит несколько элементов в одном списке. Элементы могут повторяться, порядок сохраняется.
# a = [10, 20, 30, 20]
# # append()	Добавляет элемент в конец
# a.append(40)
# print(a)
# # insert()	Добавляет элемент на указанную позицию
# a.insert(1, 15)
# print(a)
# # remove()	Удаляет указанный элемент
# a.remove(20)
# print(a)
# # pop()	Удаляет элемент с конца листа и по индексу
# a.pop()
# print(a)
# # clear()	Удаляет все элементы
# a.clear()
# print(a)
# # index()	Находит индекс элемента
# a.index(30)
# print(a.index(30))
# # count()	Считает количество повторений
# print(a.count(20))
# # sort()	Сортирует список
# a.sort()
# print(a)
# # reverse()	Переворачивает порядок элементов
# a.reverse()
# print(a)
# # copy()	Создаёт копию списка
# b = a.copy()
# print(b)
# # len()	Возвращает количество элементов
# print(len(a))
#
# # set — хранит уникальные элементы. Повторы автоматически удаляются, порядок не гарантируется.
# # a = {10, 20, 30}
# # add()	Добавляет элемент
# a.add(40)
# print(a)
# # update()	Добавляет несколько элементов
# a.update({50, 60})
# print(a)
# # remove()	Удаляет элемент, выдаёт ошибку, если его нет
# a.remove(10)
# print(a)
# # discard()	Удаляет элемент без ошибки, если его нет
# a.discard(100)
# print(a)
# # pop()	Удаляет случайный элемент
# a.pop()
# print(a)
# # clear()	Удаляет все элементы
# a.clear()
# print(a)
# # copy()	Создаёт копию множества
# b = a.copy()
# print(b)
#
# x = {1, 2, 3}
# y = {3, 4, 5}
# # union()	Объединяет множества
# print(x.union(y))
# # intersection()	Находит общие элементы
# print(x.intersection(y))
# # difference()	Находит элементы, которых нет во втором множестве
# print(x.difference(y))
# # issubset()	Проверяет, является ли множество подмножеством
# print({1, 2}.issubset({1, 2, 3}))
# # issuperset()	Проверяет, содержит ли множество другое множество
# print({1, 2, 3}.issuperset({1, 2}))
#
# # dict — хранит данные в формате ключ: значение.
# a = {"name": "Ali", "age": 17}
# # keys()	Показывает все ключи
# print(a.keys())
# # values()	Показывает все значения
# print(a.values())
# # items()	Показывает пары ключ: значение
# print(a.items())
# # get()	Получает значение по ключу
# print(a.get("name"))
# # update()	Добавляет или обновляет данные
# a.update({"age": 18})
# print(a)
# # pop()	Удаляет элемент по ключу
# a.pop("city")
# print(a)
# # popitem()	Удаляет последнюю добавленную пару
# a.popitem()
# print(a)
# # clear()	Удаляет все элементы
# a.clear()
# print(a)
# # copy()	Создаёт копию словаря
# b = a.copy()
# print(b)
# # setdefault()	Получает значение или добавляет ключ со значением по умолчанию
# a.setdefault("country", "Kazakhstan")
# print(a)
# #Придумать мини функцию с использованием методов Str
# def name_check():
#     name = input("Введите своё имя: ")
#
#     name = name.strip()
#     name = name.capitalize()
#
#     print("Привет,", name)
#     print("Количество букв:", len(name))
#     print("Имя заглавными буквами:", name.upper())
#
#
# name_check()


# def ab_sum(name, age):
#     return name, age
#
# print(ab_sum("yerkhan", 17))

# map()
# sorted()
# filter()