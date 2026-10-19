# list, tuple
# dict - словарь
d = {}
print(d)
print(type(d))
d = {"a":1, "b": 2}
d = dict()
d = dict(a=1, b=2)
d = dict([("a", 11), ("b", 22)])
print(d)
person = {
    "age": 30,
    "name": "John",
    "surname": "Doe",
    "weight_kg": 70.25,
    "is_resident": True,
    "favourite_colors": ("red", "blue", "green"),
    "visited_countries": ["China", "USA", "France"],
    "sport_results": {
        "football": "golden medal",
        "box": "ibf champ"
    },
    101: "this is 101",
    90.4523: "this element has float key",
    True: 123,
    ("a", 1, True): "abcd"
}

print(person)
temperatures = {
    20.45: "too low temp",
    36.6: "normal human temp",
    41.34: "dangerous temp"
}
print(temperatures)

years_dict = {
    1991: "USSR is over",
    1917: "October revolution",
    1939: "2nd world war started"
}
print(years_dict)

mybook = {
    "title": "Том Сойер",
    "publish_date": 1930,
    "page_qnty": 200,
    "with_hardcover": True,
    "pics_page_number": [20, 45, 100, 156]
}
print(mybook)
print(mybook["title"])
print(mybook["publish_date"])
print(mybook["pics_page_number"])
print(mybook["pics_page_number"][-1])
print(mybook["pics_page_number"][1])
# print("5th element", mybook["pics_page_number"][5])   # IndexError
# print(mybook["mykey"]) # error KeyError
print(mybook.get("mykey"))
print(mybook.get("mykey", "some key"))
print(mybook.get("page_qnty", "some key"))
print("mykey" in mybook)
print("title" in mybook)
mystring = "abcd1243asadfqwer"
print( "asdf" in mystring)
print( "qwe" in mystring)

car = dict(brand="BMW", issue_year=2025, doors_qnty=4, milage=50000)
print(car)
car["milage"] = 60000
print(car)
car["milage"] += 5000
print(car)
car["milage"] = car["milage"] + 10000
print(car)
del car["milage"]
print(car)
mycard_holder = {
    "halyk": 2,
    "kaspi": 1,
    "bcc": 4
}
print(mycard_holder)


kaspi_cards_qnty = mycard_holder.pop("kaspi34", 99)
print(mycard_holder)
print(kaspi_cards_qnty)

mystring = "asdfb"
mystring.strip()

mycard_holder.clear()
print(mycard_holder)

mywallet = {
    "500 KzT": 2,
    "1000 KZT": 4,
    "10000 KZT": 5,
    "100 USD": 5,
    "50 USD": 2,
}

sum_in_wallet = 0

# for banknote in mywallet:
for banknote in mywallet.keys():
    if "KZT" in banknote.upper():
        banknote_name_parts = banknote.split()  # ['1000', 'KZT']
        try:
            banknote_nominal_amount = int(banknote_name_parts[0])
        except ValueError:
            banknote_nominal_amount = 0
        print(banknote_nominal_amount)
        sum_in_wallet += banknote_nominal_amount * mywallet[banknote]
print(f"Amount of KZT in my wallet is {sum_in_wallet} KZT")
print(mywallet.keys())
print(mywallet.values())


sum_in_wallet = 0

for banknote, quantity in mywallet.items():
    print(banknote, "|", quantity)
    if "KZT" in banknote.upper():
        banknote_name_parts = banknote.split()  # ['1000', 'KZT']
        try:
            banknote_nominal_amount = int(banknote_name_parts[0])
        except ValueError:
            banknote_nominal_amount = 0
        print(banknote_nominal_amount)
        sum_in_wallet += banknote_nominal_amount * quantity
print(f"Amount of KZT in my wallet is {sum_in_wallet} KZT")

# Python 3.7+ - порядок сохраняется
# Python 3.9 можно делать так

mywallet1 = {
    "1000 KZT": 4,
    "100 USD": 5,
    "50 USD": 2,
}

mywallet2 = {
    "100 KZT": 7,
    "50 KZT": 20,
}

mywallet3 = mywallet1 | mywallet2
print(mywallet3)

a = 4
_a = 4
print(_a)
# list, tuple, dict

# set - множество

s = {1, 2, 3}
print(type(s))
print(s)
s = set()
print(type(s))
print(s)

banknote_nominals_list = [500, 1000, 10000, 20000, 50000, 500, 1000, 1000]    # list
banknote_nominals_set = set(banknote_nominals_list)
print(banknote_nominals_set)

# a | b - объединение
# a & b - пересечение
# a - b - разность
# a ^ b - симм. разность

a = {1, 2, 3}
b = {3, 4, 5}
c =  a | b # - объединение, Union
c =  a & b # - пересечение, Intersection
c =  a - b # - разность, Subtraction
c =  b - a # - разность, Subtraction
c =  a ^ b # - симм. разность, Simmetrical Difference
c = a.union(b)
print(c)

c = {1, 2, 3, 4, 5}
print(c)
c.add(77)
print(c)
c.add(1)
print(c)
c.remove(3)
print(c)
# c.remove(8)
c.discard(8)
print(c)
set_element = c.pop()
print(c)
print(set_element)
set_element = c.pop()
print(c)
print(set_element)
set_element = c.pop()
print(c)
print(set_element)
c = {"a", "b", "c"}
print(c)
c.clear()
print(c)

c = {1, 2, 3, 4, 5}
for set_element in c:
    print(set_element)

mulitplication = 1
for set_element in c:
    mulitplication = mulitplication * set_element

print(mulitplication)
print(len(c))
print(mywallet3)
print(len(mywallet3))
mylist = [1, 2, 3]
print(mylist)
print(len(mylist))
mytupple = (3,)
print(mytupple)
print(len(mytupple))

print(len("asdfbcdfadsf"))

# enumerate()

fruits = ["apple", "orange", "mango"]
print(fruits)
print(enumerate(fruits))

for i, frt in enumerate(fruits, start=2):
    print(i, frt)

print("-"*10)
for i, frt in enumerate(fruits, start=1):
    print(f"{i}. {frt}")

# zip
names = ["Bob", "John", "Ann", "Martin"]
ages = [23, 19, 40, 80]
heights = [170, 180, 160, 175]

print(zip(names, ages))
print(list(zip(names, ages, heights)))

for name, age in zip(names, ages):
    print(name, age)

students = dict(zip(names, ages))
print(students)

[1, 2, 3,]
(1, 2, 3,)
{1, 2, 3,}
{
    "a": 1,
    "b": 2,
    "c": 3,
}
