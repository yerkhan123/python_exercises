"""
1. Анализ оценок класса
(list, for, if, dict, set)

grades = [5, 4, 3, 5, 2, 4, 5, 3, 4, 5, 2, 4]

Выведи:

количество каждой оценки через dict + for ({5: 4, 4: 4, 3: 2, 2: 2})
средний балл
список уникальных оценок через set, отсортированный
сколько отличников (пятёрок)

Ожидаемый вывод:

Оценки: {5: 4, 4: 4, 3: 2, 2: 2}
Средний балл: 4.0
Уникальные: [2, 3, 4, 5]
Пятёрок: 4
"""
grades = [5, 4, 3, 5, 2, 4, 5, 3, 4, 5, 2, 4]

counts = {}

for grade in grades:
    if grade in counts:
        counts[grade] += 1
    else:
        counts[grade] = 1

average = sum(grades) / len(grades)

unique = sorted(set(grades))

fives = 0

for grade in grades:
    if grade == 5:
        fives += 1

print("Оценки:", counts)
print("Средний балл:", average)
print("Уникальные:", unique)
print("Пятёрок:", fives)
#=====================================================================
"""
2. Частотный словарь слов
(str methods, split, dict, for, sorted)

text = "python это язык python простой и python мощный"
Приведи к нижнему регистру.

Разбей на слова через split().
Посчитай частоту каждого слова в dict.
Выведи топ-3 по частоте (через sorted с key или вручную).

Ожидаемый вывод:

text
Слова: {'python': 3, 'это': 1, 'язык': 1, 'простой': 1, 'и': 1, 'мощный': 1}
Топ-3: [('python', 3), ('это', 1), ('язык', 1)]
Подсказка: для сортировки — sorted(d.items(), key=lambda x: -x[1]), но если lambda не проходили, отсортируй вручную.
"""
text = "python это язык python простой и python мощный"

text = text.lower()

words = text.split()

counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

sorted_words = sorted(counts.items(), key=lambda x: -x[1])

print("text")
print("Слова:", counts)
print("Топ-3:", sorted_words[:3])
#=====================================================================
"""
3. Общие друзья
(set, set operations)

anna_friends = {"Борис", "Вера", "Глеб", "Даша"}
boris_friends = {"Вера", "Глеб", "Егор", "Жанна"}
Выведи:

общих друзей (&)
всех знакомых (|)
только Анниных (-)
тех, кто есть только у одного (^)
"""
anna_friends = {"Борис", "Вера", "Глеб", "Даша"}
boris_friends = {"Вера", "Глеб", "Егор", "Жанна"}

print("Общие друзья:", anna_friends & boris_friends)
print("Все знакомые:", anna_friends | boris_friends)
print("Только Аннины:", anna_friends - boris_friends)
print("Только у одного:", anna_friends ^ boris_friends)
#=====================================================================
"""
4. Журнал ошибок
(try/except, file write, while, if)

В цикле while True проси ввести число. Пока не введено stop:
если число — запиши его в ok.txt
если не число — запиши в errors.txt строку вида "abc (не число)"

В конце выведи количество успешных и ошибочных строк.
"""
ok_count = 0
error_count = 0

while True:
    value = input("Введите число или stop: ")

    if value == "stop":
        break

    try:
        number = int(value)

        file = open("ok.txt", "a")
        file.write(value + "\n")
        file.close()

        ok_count += 1

    except ValueError:
        file = open("errors.txt", "a")
        file.write(value + " (не число)\n")
        file.close()

        error_count += 1

print("Успешных:", ok_count)
print("Ошибочных:", error_count)
#=====================================================================
"""
5. Меню с номерами и выбором
(enumerate, list, if, input)

menu = ["Плов", "Лагман", "Манты", "Шашлык", "Чай"]

Выведи меню с номерами через enumerate.
Спроси номер блюда.
Если номер в диапазоне — выведи "Вы выбрали: X".
Иначе — "Такого блюда нет".
"""
menu = ["Плов", "Лагман", "Манты", "Шашлык", "Чай"]

for number, dish in enumerate(menu, start=1):
    print(f"{number}. {dish}")

choice = int(input("Выберите номер блюда: "))

if choice >= 1 and choice <= len(menu):
    print(f"Вы выбрали: {menu[choice - 1]}")
else:
    print("Такого блюда нет")
#=====================================================================
"""
6. Параллельные списки
(zip, list, for, if)

names = ["Аня", "Борис", "Вера", "Глеб"]
grades = [5, 3, 4, 2]

Выведи:

пары имя - оценка (через zip)
только тех, у кого >= 4
средний балл

Ожидаемый вывод:

Аня - 5
Борис - 3
Вера - 4
Глеб - 2
Хорошисты: Аня, Вера
Средний: 3.5
"""
names = ["Аня", "Борис", "Вера", "Глеб"]
grades = [5, 3, 4, 2]

good_students = []

for name, grade in zip(names, grades):
    print(f"{name} - {grade}")

    if grade >= 4:
        good_students.append(name)

average = sum(grades) / len(grades)

print("Хорошисты:", ", ".join(good_students))
print("Средний:", average)