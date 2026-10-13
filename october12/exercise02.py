"""
 1. Сумма двух чисел. Запроси два числа через input(), выведи сумму.
"""

nuber1_str = input("Please input integer number (int):")

number1_str = input("Please input integer number 1(int):")
try:
    number1 = int(number1_str)
    number2_str = input("Please input integer number 2(int):")
    try:
        number2 = int(number2_str)
        number_sum = number1 + number2
        print(f"Sum of {number1} and {number2} is {number_sum}")
    except ValueError as e:
        print("Sorry, number 2 is not an integer number!")
        print("Please try again")

except ValueError as e:
    print("Sorry, number 1 is not an integer number!")
    print("Please try again")

