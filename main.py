# int           Целое число  42, -10
# float         Число с плавающей точкой  3.14, -0.5
# bool          Логическое значение  True, False
# str           Строка  "Привет"
# list          Список  [1, 2, 3]
# tuple         Кортеж  (1, 2, 3)
# range         Последовательность целых чисел  range(5)
# dict          Словарь: пары «ключ — значение»  {"имя": "Анна", "возраст": 25}
# set           Множество уникальных элементов  {1, 2, 3}
# frozenset     Неизменяемое множество  frozenset({1, 2, 3})

# complex       Комплексное число  2 + 3j
# bytes         Неизменяемая последовательность байтов  b"hello"
# bytearray     Изменяемая последовательность байтов  bytearray(b"hello")
# memoryview    Представление данных в памяти без копирования  memoryview(b"hello")
# NoneType      Отсутствие значения  None

# Неизменяемые типы:
# числа, bool, str, tuple, range, frozenset, bytes, NoneType.

# Изменяемые типы:
# list, dict, set, bytearray

# #str - именения регистра
# text = "Hello World"
#
# #Первый символ в верхний
# #Регистр остальное ы нижний
# print(text.capitalize())
#
# #Все в ниж-регистре
# print(text.lower())
# #Все в верх-регитре
# print(text.upper())
#
# #Все заглавные буква в верх-регистре
# print(text.title())
#
# # Меняет верхний регистр
# # на нижний и наобарот
# print(text.swapcase())

#str - методы проверки содержимого
# text = "abc 123"
#
# #Строка непустая и состоит только из букв и числовых символов
# print(text.isalnum())
#
# #Строка непустая и состоит только из букв
# print(text.isalpha())
#
# #Все символы относятся к ASCII для пустой строки тоже True
# print(text.isascii())
#
# # Строка непустая и состоит только из десятичных цифр
# print(text.isdecimal())
#
# # Строка непустая и состоит только из цифр
# print(text.isdigit())
#
# # Строка непустая и состоит только из числовых символов
# print(text.isnumeric())
#
# # Строка имеет допустимую форму идентификатора Python
# print(text.isidentifier())
#
# # Все буквы строчные
# print(text.islower())
#
# # Есть буквы заглавные
# print(text.isupper())
#
# # Все слова с заглавной
# print(text.istitle())
#
# # Стрка непустая и состоит только из пробельных символов
# print(text.isspace())
#
# # Все символы печатаемые для пустой строки тоже True
# print(text.isprintable())
#
#
# # str - Удаления символов
# text = " hello "
#
# # Удаляет символы с обоих краёв по умолчанию пробельные
# print(text.strip())
# # Удаляет символы слева по умолчанию пробельные
# print(text.lstrip())
# # Удаляет символы справа по умолчанию пробельные
# print(text.rstrip())
#
# print(text.strip("H"))
# print(text.lstrip("H"))
# print(text.rstrip("H"))
#
# print("www.kaspi.kz".removeprefix("www."))
# print("www.kaspi.kz".removesuffix(".kz"))

# str - Замена и преобразования
# text = "he11o"
#
# # Что заменить и на что заменить
# print(text.replace("1", "l"))
#
# # str - выравнивания и заполнения
# text = "he11o"
#
# # Вравнивает по центру
# print(text.center(10, "*"))
# # Вравнивает по левому краю
# print(text.ljust(10, "*"))
# # Выравнивает по правому краю
# print(text.rjust(10, "*"))
#
# # Дополняет слева нулями, учитывая знак числа
# print(text.zfill(10))
#
#
# # str - Форматирование
# # text = "Привет {}, забранируй место на {}"
#
# # Подставляет значения в поля {}
# # print(text.format("Yerkhan", "19:00"))
# #
# #
# # print(text.format(name="Yerkhan", time="19:00"))
# # text = "Привет {name}, забранируй место на {time}"
#
# name = "Yerkhan"
# age = 17
#
# print(f"Привет {name}, забранируй место на {age}")
#
# # str - поиск и подсчет
#
# text = "Привет {name}, забранируй место на {time}"
#
# # считает подстроки в строке
# print(text.count("и"))
#
# # проверяет начало строки
# print(text.startswith("Привет"))
# # проверяет конец строки
# print(text.endswith("}"))
#
# # Возвращает индекс подстроки при отсуствии ValueError
# print(text.index("и"))
# # Ищет с конца
# print(text.rindex("и"))
#
# # Возвращает индекс подстроки при отсуствии вернет -1
# print(text.find("и"))
# # ищет с конца
# print(text.rfind("и"))

# str - Срезы
# [start, stop, shag]
#  0  1  2  3  4  5
#  П  р  и  в  е  т
# -6 -5 -4 -3 -2 -1
print("Привет"[2:])
print("Привет"[:3])
print("Привет"[::-1])

# Домашка на сб
# Так же как на уроке разберите методы List, Set, Dict
# Придумать мини функцию с использованием методов Str
