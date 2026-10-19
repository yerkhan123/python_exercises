"""
1. Телефонный справочник с сохранением
(dict, file, try/except, while, str methods)

Программа:

При старте читает contacts.txt (формат: Имя:номер по строке) и загружает в dict.

В цикле показывает меню:

1 - добавить
2 - найти
3 - удалить
4 - показать все
5 - сохранить и выйти

Операции:

добавить: спросить имя и номер, положить в dict
найти: спросить имя, вывести номер или «не найден»
удалить: спросить имя, удалить через pop с обработкой
показать все: перебрать for k, v in dict.items()
При выходе — записать весь dict в contacts.txt.
Тренирует: dict + файлы + try/except + while + строковые методы.
Ожидаемая структура contacts.txt:

Аня:+7-701-111-22-33
Борис:+7-702-444-55-66
"""
contacts = {}

try:
    with open("contacts.txt", "r", encoding="utf-8") as f:
        for line in f:
            name, number = line.strip().split(":")
            contacts[name] = number
except FileNotFoundError:
    pass

while True:
    print("\n1 - добавить")
    print("2 - найти")
    print("3 - удалить")
    print("4 - показать все")
    print("5 - сохранить и выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Имя: ")
        number = input("Номер: ")
        contacts[name] = number
        print("Контакт добавлен")

    elif choice == "2":
        name = input("Имя: ")
        print(contacts.get(name, "не найден"))

    elif choice == "3":
        name = input("Имя: ")

        try:
            contacts.pop(name)
            print("Контакт удалён")
        except KeyError:
            print("Контакт не найден")

    elif choice == "4":
        for k, v in contacts.items():
            print(k, ":", v)

    elif choice == "5":
        with open("contacts.txt", "w", encoding="utf-8") as f:
            for k, v in contacts.items():
                f.write(k + ":" + v + "\n")

        print("Сохранено!")
        break
#--------------------------------------------------------------------------
"""
2. Анализатор текстового файла
(file read, str methods, dict, set, for, sorted)

Дан файл text.txt с текстом (можешь положить туда пару абзацев сам).

Программа:

Читает файл построчно через for line in f.

Считает:
количество строк
количество слов
количество уникальных слов (через set)
самое частое слово (через dict + max)
самое длинное слово
количество знаков препинания (через in по строке ".,!?;:")
Выводит отчёт.

Ожидаемый вывод:

=== АНАЛИЗ ТЕКСТА ===
Строк: 5
Слов: 87
Уникальных слов: 54
Самое частое: "и" (7 раз)
Самое длинное: "программирование"
Знаков препинания: 12
Тренирует: файлы + строки + dict + set + for + sorted.
"""
words = []
word_count = {}
lines = 0
punctuation = 0

with open("text.txt", "r", encoding="utf-8") as f:
    for line in f:
        lines += 1

        for symbol in line:
            if symbol in ".,!?;:":
                punctuation += 1

        line = line.lower()

        for symbol in ".,!?;:":
            line = line.replace(symbol, "")

        for word in line.split():
            words.append(word)

            word_count[word] = word_count.get(word, 0) + 1

unique_words = set(words)

most_common = max(word_count, key=word_count.get)
longest_word = max(words, key=len)

print("=== АНАЛИЗ ТЕКСТА ===")
print("Строк:", lines)
print("Слов:", len(words))
print("Уникальных слов:", len(unique_words))
print("Самое частое:", most_common, "(", word_count[most_common], "раз)")
print("Самое длинное:", longest_word)
print("Знаков препинания:", punctuation)
#--------------------------------------------------------------------------
"""
3. Угадай число с рекордами
(random, while, try/except, file)

Программа:

Читает best.txt (там хранится лучший результат в попытках). Если файла нет — лучший = бесконечность.

Компьютер загадывает число 1–100 через random.randint.
В цикле while True спрашивает угадывание:
try/except для числа
подсказки «больше» / «меньше»
считает попытки
при победе — break
Если новое число попыток меньше сохранённого — обновить best.txt.
Вывести: «Ты угадал за N попыток. Рекорд: M».

Тренирует: random + while + try/except + файлы + if.
Бонус: добавь отказ от игры, если введено "stop" (через break).
"""
import random

try:
    with open("best.txt", "r") as f:
        best = int(f.read())
except FileNotFoundError:
    best = float("inf")

number = random.randint(1, 100)
attempts = 0

print("Я загадал число от 1 до 100.")

while True:
    answer = input("Твоё число: ")

    if answer.lower() == "stop":
        print("Игра закончена.")
        break

    try:
        guess = int(answer)
    except ValueError:
        print("Введите число!")
        continue

    attempts += 1

    if guess < number:
        print("Больше")
    elif guess > number:
        print("Меньше")
    else:
        print("Ты угадал за", attempts, "попыток.")

        if attempts < best:
            best = attempts

            with open("best.txt", "w") as f:
                f.write(str(best))

            print("Новый рекорд!")

        print("Рекорд:", best)
        break
#--------------------------------------------------------------------------
"""
4. Система голосования
(list, dict, set, enumerate, for, zip, file)

Данные:

votes = ["Аня", "Борис", "Аня", "Вера", "Аня", "Борис", "Глеб", "Аня", "Вера"]
Каждый элемент — за кого проголосовали.

Программа:

Посчитай голоса каждого в dict через for + .get(k, 0) + 1.
Выведи результаты, отсортированные по убыванию голосов.
Найди победителя (max по значению).
Выведи список уникальных кандидатов через set.
Выведи список тех, кто голосовал (например, ["Избиратель 1", ...]) через enumerate.
Сохрани результаты в results.txt в формате Имя: N голосов.

Ожидаемый вывод:

=== РЕЗУЛЬТАТЫ ===
Аня: 4
Вера: 2
Борис: 2
Глеб: 1

Победитель: Аня
Кандидаты: {'Аня', 'Борис', 'Вера', 'Глеб'}
Тренирует: dict + set + enumerate + for + файлы.
"""
votes = ["Аня", "Борис", "Аня", "Вера", "Аня",
         "Борис", "Глеб", "Аня", "Вера"]

results = {}

for name in votes:
    results[name] = results.get(name, 0) + 1

sorted_results = sorted(
    results.items(),
    key=lambda x: x[1],
    reverse=True
)

print("=== РЕЗУЛЬТАТЫ ===")

for name, count in sorted_results:
    print(name + ":", count)

winner = max(results, key=results.get)

print("\nПобедитель:", winner)
print("Кандидаты:", set(votes))

print("\nИзбиратели:")

for i, name in enumerate(votes, 1):
    print("Избиратель", i, "->", name)

with open("results.txt", "w", encoding="utf-8") as f:
    for name, count in sorted_results:
        f.write(name + ": " + str(count) + " голосов\n")
#--------------------------------------------------------------------------
"""
5. Дневник тренировок
(file, dict, try/except, while, zip, enumerate)

Программа:

Читает файл training.txt (формат: дата:упражнение:подходы:повторы).
Пример:

Пн:приседания:3:10
Пн:жим:4:8
Ср:тяга:3:6
Загружает в dict где ключ — день, значение — список упражнений.

В цикле показывает меню:

1 - добавить тренировку
2 - показать по дню
3 - показать всё
4 - общее число упражнений
5 - сохранить и выйти

При добавлении — спросить данные и записать в dict.
При показе по дню — перебрать упражнения через enumerate.
При выходе — сохранить обратно в файл.
Тренирует: файлы + dict + list + enumerate + while + try/except.

Бонус: при загрузке файла — если строка битая (мало полей), пропустить через try/except + continue.
"""
#--------------------------------------------------------------------------
training = {}

try:
    with open("training.txt", "r", encoding="utf-8") as f:
        for line in f:
            try:
                day, exercise, sets, reps = line.strip().split(":")

                if day not in training:
                    training[day] = []

                training[day].append([exercise, sets, reps])

            except ValueError:
                continue

except FileNotFoundError:
    pass

while True:
    print("\n1 - добавить тренировку")
    print("2 - показать по дню")
    print("3 - показать всё")
    print("4 - общее число упражнений")
    print("5 - сохранить и выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        day = input("День: ")
        exercise = input("Упражнение: ")

        try:
            sets = int(input("Подходы: "))
            reps = int(input("Повторы: "))
        except ValueError:
            print("Введите число!")
            continue

        if day not in training:
            training[day] = []

        training[day].append([exercise, sets, reps])

    elif choice == "2":
        day = input("День: ")

        if day in training:
            for i, exercise in enumerate(training[day], 1):
                print(i, exercise[0],
                      "-", exercise[1], "подхода",
                      "-", exercise[2], "повторов")
        else:
            print("Такого дня нет")

    elif choice == "3":
        for day, exercises in training.items():
            print("\n", day)

            for exercise in exercises:
                print(
                    exercise[0],
                    "-", exercise[1],
                    "подхода -",
                    exercise[2],
                    "повторов"
                )

    elif choice == "4":
        total = 0

        for exercises in training.values():
            total += len(exercises)

        print("Всего упражнений:", total)

    elif choice == "5":
        with open("training.txt", "w", encoding="utf-8") as f:
            for day, exercises in training.items():
                for exercise in exercises:
                    f.write(
                        day + ":" +
                        exercise[0] + ":" +
                        str(exercise[1]) + ":" +
                        str(exercise[2]) + "\n"
                    )

        print("Сохранено!")
        break
