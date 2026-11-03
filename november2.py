# 1. Исправление списка гостей
#from october19.homework1 import unique_words

# guests = ["  аЛи ", "АННА", "али", "  иВАН", "анна  "]
# Напиши функцию prepare_guests(guests), которая:
# - Удаляет пробелы по краям и приводит имена к виду "Али".
# - Убирает повторяющиеся имена.
# - Возвращает список имён по алфавиту.
# Ожидаемый результат:
# ["Али", "Анна", "Иван"]
# Используй методы строк, map(), set() и sorted().
# guests = ["  аЛи ", "АННА", "али", "  иВАН", "анна  "]
#
# def prepare_guests(guests):
#
#     guests = list(map(lambda name: name.strip().capitalize(), guests))
#     guests = set(guests)
#     guests = sorted(guests)
#
#     return guests
#
#
# result = prepare_guests(guests)
# print(result)

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

# queue = ["Али", "Анна", "Иван", "Мария"]
#
# queue.append("Олег")
# queue.insert(1, "Вера")
# queue.remove("Иван")
# served = queue.pop(0)
#
# maria = queue.index("Мария") + 1
#
# print("Обслужен:", served)
# print("Итоговая очередь:", queue)
# print("Место Марии:", maria)

# 3. Фильтр правильных имён
# names = ["Анна", "иван", "123", "", "Олег!", "  Мария  ", "Ян"]
# Напиши функцию valid_names(names), которая очищает пробелы и оставляет только имена, состоящие из букв и содержащие не менее трёх символов. Приведи имена к виду "Анна".

# Ожидаемый результат:
# ["Анна", "Иван", "Мария"]
# Используй strip(), isalpha(), len(), map() и filter().

# names = ["Анна", "иван", "123", "", "Олег!", "  Мария  ", "Ян"]
#
# def valid_names(names):
#
#     names = list(map(lambda name: name.strip().capitalize(), names))
#
#     names = list(filter(lambda name: name.isalpha() and len(name) >= 3, names))
#
#     return names
#
#
# result = valid_names(names)
# print(result)

# 4. Общие интересы
# ali = {"Python", "шахматы", "музыка", "кино"}
# anna = {"музыка", "рисование", "Python", "танцы"}
# Найди:
# - Общие интересы.
# - Все интересы двух друзей.
# - Интересы, которые есть только у Али.
# - Интересы, которые есть только у Анны.
# - Есть ли у обоих интересы "Python" и "музыка".
# Для удобства выводи полученные множества как списки по алфавиту.

# Используй intersection(), union(), difference() и issubset().

# ali = {"Python", "шахматы", "музыка", "кино"}
# anna = {"музыка", "рисование", "Python", "танцы"}

# common = ali.intersection(anna)
# all_interests = ali.union(anna)
# ali = ali.difference(anna)
# anna = anna.difference(ali)

# check = {"Python", "музыка"}.issubset(ali) and {"Python", "музыка"}.issubset(anna)

# print("Общие интересы:", sorted(common))
# print("Все интересы:", sorted(all_interests))
# print("Только у Али:", sorted(ali))
# print("Только у Анны:", sorted(anna))
# print("Python и музыка есть у обоих:", check)




# 5. Анализ сообщения
# text = "  Python это интересно python это полезно Python  "
# Напиши функцию analyze_text(text), которая приводит текст к нижнему регистру, разбивает его на слова и возвращает словарь:
# {
#     "words": 8,
#     "unique_words": 5,
#     "python_count": 3
# }
# Используй lower(), split(), set(), count() и len().

text = "  Python это интересно python это полезно Python  "

def analyze_text(text):
    text = text.lower()
    words = text.split()

    result = {
        "words": len(words),
        "unique_words": len(set(words)),
        "python_count": words.count("python")
    }

    return result

print(analyze_text(text))

# 6. Обновление профиля игрока
# player = {
#     "name": "  аЛи ",
#     "level": 3,
#     "city": "Алматы",
#     "temporary": True
# }
# Напиши функцию update_profile(player), которая создаёт копию словаря и в ней:
# - Исправляет имя на "Али".
# - Повышает уровень на один.
# - Удаляет ключ "temporary".
# - Добавляет "country": "Kazakhstan", только если такого ключа ещё нет.
# Верни обновлённый словарь. Исходный player должен сохранить прежние данные.

# Используй copy(), методы строк, update(), pop() и setdefault().

player = {
    "name": "  аЛи ",
    "level": 3,
    "city": "Алматы",
    "temporary": True
}

def update_profile(player):
    new_player = player.copy()

    new_player["name"] = new_player["name"].strip().capitalize()

    new_player["level"] += 1

    new_player.pop("temporary")

    new_player.setdefault("country", "Kazakhstan")

    return new_player


updated_player = update_profile(player)

print("Обновлённый:", updated_player)
print("Исходный:", player)