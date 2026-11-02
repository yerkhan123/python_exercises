# 1. Исправление списка гостей

# guests = ["  аЛи ", "АННА", "али", "  иВАН", "анна  "]
# Напиши функцию prepare_guests(guests), которая:
# - Удаляет пробелы по краям и приводит имена к виду "Али".
# - Убирает повторяющиеся имена.
# - Возвращает список имён по алфавиту.
# Ожидаемый результат:
# ["Али", "Анна", "Иван"]
# Используй методы строк, map(), set() и sorted().
guests = ["  аЛи ", "АННА", "али", "  иВАН", "анна  "]

def prepare_guests(guests):

    guests = list(map(lambda name: name.strip().capitalize(), guests))
    guests = set(guests)
    guests = sorted(guests)

    return guests


result = prepare_guests(guests)
print(result)

# 2. Управление очередью
# queue = ["Али", "Анна", "Иван", "Мария"]
# Выполни события по порядку:
# В очередь встал Олег.
# Вера заняла место сразу после Али.
# Иван ушёл из очереди.
# Первого человека обслужили — сохрани его имя.
# Найди позицию Марии в очереди, считая места с единицы.
# Выведи имя обслуженного человека, итоговую очередь и место Марии.
# Используй append(), insert(), remove(), pop() и index().

queue = ["Али", "Анна", "Иван", "Мария"]

queue.append("Олег")
queue.insert(1, "Вера")
queue.remove("Иван")
served = queue.pop(0)

maria = queue.index("Мария") + 1

print("Обслужен:", served)
print("Итоговая очередь:", queue)
print("Место Марии:", maria)

# 3. Фильтр правильных имён
# names = ["Анна", "иван", "123", "", "Олег!", "  Мария  ", "Ян"]
# Напиши функцию valid_names(names), которая очищает пробелы и оставляет только имена, состоящие из букв и содержащие не менее трёх символов. Приведи имена к виду "Анна".

# Ожидаемый результат:
# ["Анна", "Иван", "Мария"]
# Используй strip(), isalpha(), len(), map() и filter().

names = ["Анна", "иван", "123", "", "Олег!", "  Мария  ", "Ян"]

def valid_names(names):

    names = list(map(lambda name: name.strip().capitalize(), names))

    names = list(filter(lambda name: name.isalpha() and len(name) >= 3, names))

    return names


result = valid_names(names)
print(result)