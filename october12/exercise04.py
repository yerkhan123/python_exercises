"""
Среднее из трёх. Три числа вводятся с консоли.
"""
number1_str = input("Please input integer number 1(int):")
try:
    number1 = int(number1_str)
    number2_str = input("Please input integer number 2(int):")
    try:
        number2 = int(number2_str)
        number3_str = input("Please input integer number 3(int):")
        try:
            number3 = int(number3_str)
            number_avg = (number1 + number2 + number3) / 3
            print(f"Average is {number_avg}")
        except ValueError as e:
            print("Sorry, number 3 is not an integer number!")
            print("Please try again")
    except ValueError as e:
        print("Sorry, number 2 is not an integer number!")
        print("Please try again")
except ValueError as e:
    print("Sorry, number 1 is not an integer number!")
    print("Please try again")