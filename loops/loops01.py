# циклы
# цикл while
i = 1
while i <= 5:
    print(i, 'Hello!')
    i += 1 # i = i + 1
    # i -= 23
    # i *= 4
    # i *= i # i = i * i
    # i %= 2

print('program finished!')
b = 10
c = 22
if b == 10 and c == 20:
    print("+")
else:
    print("-")

# 1. **
# 2. * /
# 3. + -
"""
(1 + 2) * 3
(a > 3) and (b < 10)
not a > 3 and not b < 10
"""
# ()
# not
# and
# or

# булева логика or (логическое ИЛИ)
# bool, boolean
"""
True or True   -> True
True or False  -> True
False or True  -> True
False or False -> False
"""
# булева логика and (логическое И)
"""
True and True   -> True
True and False  -> False
False and True  -> False
False and False -> False
"""
# булева логика not (логическое НЕ)
"""
not True  -> False
not False -> True
"""

i = 1
while i <= 5:
    print(i, 'Hello!')
    i += 1

# цикл for - для перебора коллекций (list, tuple, str)
# str
print("цикл for")
string1 = "abcd"
for c in string1:
    print(c * 4)

print("finish")
list1 = [1, 2, "asdf", 45.45]
for element in list1:
    print(element)

print("finish2")

tuple1 = ('word1', 'asdfasdfa', '23423423')
for word in tuple1:
    print(len(word))

print("finish3")
# range
print(range(4))

for i in range(10):
    print(i)

for _ in range(10):
    print("Hello!")

for i in range(2, 7):
    print(i)

print("range with 3 parameters")
for i in range(2, 10, 3):
    print(i)

print("range with 3 parameters")
for i in range(10, 2, -2):
    print(i)

print('введите целые числа и закончите ввод числом 0')
# mylist = []
# mynumber = "1"
# while mynumber != "0":
#     mynumber = input('введите число:')
#     mylist.append(mynumber)
#
# print(mylist)

# break и continue
i = 0
while True:
   if i == 5:
       break
   else:
       print(i)
   i = i + 1
print('finish')
# continue

i = 0
while i <= 10:
   i = i + 1
   if i % 2 == 0:
       continue
   print(i)
   i = i + 1
print('finish continue')