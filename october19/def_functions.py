def sum_and_multipl(num1, num2):
    sum_of_two = num1 + num2
    multipl_of_two = num1 * num2
    return sum_of_two, multipl_of_two


def sum_two_int_number(number1, number2):
    if number1 < 0 or number2 < 0:
        return None

    sum_of_two = number1 + number2
    return sum_of_two


def sum_two_int_number(number1: int, number2: int) -> int:
    """
    docstring
    функция сложения двух положительных целых чисел
    :param number1: первое число
    :param number2: второе число
    :return: сумма чисел
    """
    if number1 < 0 or number2 < 0:
        return None

    sum_of_two = number1 + number2
    return sum_of_two


a1 = sum_two_int_number(10, 12)
print('a1', a1)
a2 = sum_two_int_number(12356, 20002323)
print('a2', a2)
print(sum_two_int_number(12356, 20002323))

print('a3', sum_two_int_number(2.45, 50.66))
# print('a4', sum_two_int_number("abc", "HGF"))
# print('void:', type(sum_two_int_number("abc", "HGF")))

print(sum_and_multipl(10, 2))

def say_hello(greeting, myname="NoName", howmanytimes=1):
    print(f"{greeting} {myname}!" * howmanytimes)
    print("-" * 10)

say_hello("Hellllo", "John")
say_hello("HELLLLO", "Anna")
say_hello("Привет", "Anna", 3)
say_hello("Салем")

def get_3_max_values_from_list(mylist, addition_list=[]):
    """
    функция принимает список целых чисел и возвращает 3 самых максимальных числа
    """
    mylist.extend(addition_list)
    mylist.sort(reverse=True)
    return mylist[:3]

print(
    get_3_max_values_from_list([5, 1, 7, 9, 2], [56, 2, 5])
)

print(
    get_3_max_values_from_list([5, 1, 7, 9, 2])
)

def myfunction1(number, mylist = []):
    mylist.append(number)
    print(mylist)

def myfunction(number, mylist = None):
    if not mylist:
        mylist = []
    mylist.append(number)
    print(mylist)

myfunction(1)
myfunction(2)
myfunction(3)
myfunction(4, [55, 66])



def count_my_money(mywallet):
    """
    {'KZT': 55000, 'USD': 600, 'EURO': 1200, 'ЮАНЬ': 100}
    """
    result = dict()

    for banknote, quantity in mywallet.items():
        banknote_normalized_key = banknote.upper()
        banknote_name_parts = banknote_normalized_key.split()  # ['1000', 'KZT']
        try:
            banknote_nominal_amount = int(banknote_name_parts[0])
        except ValueError:
            banknote_nominal_amount = 0
        banknote_currency = banknote_name_parts[1]
        current_banknote_sum_amount = result.setdefault(banknote_currency, 0)
        current_banknote_sum_amount  += banknote_nominal_amount * quantity
        result[banknote_currency] = current_banknote_sum_amount

    return result

mywallet = {
    "500 KzT": 2,
    "1000 KZT": 4,
    "10000 KZT": 5,
    "100 USD": 5,
    "50 USD": 2,
    "50 EURo": 4,
    "100 euro": 10,
    "10 юань": 10,
}
mywallet1 = {
    "50 фунтов": 20,
    "100 дирхамов": 15,
    "200 дирхамов": 1,
    "10 фунтов": 4,
}
{'KZT': 55000, 'USD': 600, 'EURO': 1200, 'ЮАНЬ': 100}
print(count_my_money(mywallet))
print(count_my_money(dict()))
print(count_my_money(mywallet1))

x = 10
def myfunction1():
    x = 34
    print('in function', str(x))

myfunction1()
print(x)

def outer():
    def inner(a):
        return a * 2

    x = 12
    a = x * 10
    b = inner(a)
    return b

myresult = outer()
print(myresult)