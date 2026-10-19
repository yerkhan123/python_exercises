#1. Создай список из 5 любимых фильмов. Выведи его и его длину.
movies = ["Черный адам", "Аватар", "Интерстеллар", "Мстители", "Люди икс"]

print(movies)
print(len(movies))

#2. Дан список [10, 20, 30, 40, 50]. Выведи первый, последний элемент и срез [1:4].
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[-1])
print(numbers[1:4])

#3. Создай пустой список. В цикле for добавь 3 числа через input и добавь его в список с помощью функции append. Выведи результат.
numbers = []

for i in range(3):
    number = int(input("Введите число: "))
    numbers.append(number)

print(numbers)

#4. Дан список [3, 1, 4, 1, 5]. Отсортируй его через sort(), потом выведи. Затем сделай sorted копию и сравни.
numbers = [3, 1, 4, 1, 5]

numbers.sort()
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)

print(numbers == sorted_numbers)

#5. Дан список [1, 2, 3]. Сделай копию через .copy(), измени оригинал — копия не должна поменяться.
numbers = [1, 2, 3]

copy_numbers = numbers.copy()

numbers.append(4)

print(numbers)
print(copy_numbers)

#6. Дан список [5, 3, 8, 1, 9]. Выведи sum, min, max, len.
numbers = [5, 3, 8, 1, 9]

print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(len(numbers))