"""
0. Ввести с консоли строку представляющую целое число с помощью функции input().
Произвести перевод данной строки в число с помощью функции явного приведения типов - int().
Функцию int() обрамить в try except - если введенная строка не является строковым представлением целого числа - то вывести в консоль сообщение «Это не число».
"""

nuber_str = input("Please input integer number (int):")

try:
    number = int(nuber_str)
except ValueError as e:
        print("sorry, but you need to input an integer")
        print("please try again")
        print(e)
        number = None

print(f"You entered number: {number}")