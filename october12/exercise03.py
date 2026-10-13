"""
Периметр прямоугольника. Запроси длину и ширину, выведи 2 * (a + b).
"""

length_str = input("Please input the length (int):")
try:
    length = int(length_str)
    width_str = input("Please input the width (int):")
    try:
        width = int(width_str)
        area = 2 * (length + width)
        print(f" Area of the rectanble is {area}")
    except ValueError as e:
        print("Sorry, number 2 is not an integer number!")
        print("Please try again")

except ValueError as e:
    print("Sorry, number 1 is not an integer number!")
    print("Please try again")