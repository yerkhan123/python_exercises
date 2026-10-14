# list - список
from tabnanny import filename_only

s = 'abcd'
s = 'abcd'
print(s)
print(len(s))
print(s[0])
print("this is a list:")
l = [12, 34, 65, 78]
print(l)
print(len(l))
print(l[0])
l = [34, 'asdf', 45.67, True, None, False, [1, 2, 3]]
print(l)
print(len(l))
print(l[0])
print(l[2])
print(l[-1])
print(l[-1][1])
list2 = [2, 3, 4, 5, 6]
list2.extend([20, 21, 22])
print(list2)

# append -

# insert - вставка
len(list2)
list2.append(40)
print(list2)
list2.insert(2, 40)
print(list2)
list2.insert(-2, 77)
print(list2)

# remove - удаление
list2.remove(2)
print(list2)
list2.remove(20)
print(list2)
del list2[3]
print(list2)
a = list2.pop()
print(list2)
print(a)
b = list2.pop(2)
print(list2)
print(b)
list3 = []
list4 = list()
print(list3)
print(type(list3))
print(list4)
# сортировка
list5 = [6, 7, 10, 8, 9]
print(list5)
list5.sort()
print(list5)
list5.sort(reverse=True)
print(list5)
list6 = ['c', 'b', 'a', 'df']
list6.sort(reverse=False)
print(list6)
list7 = [103, 101, 104, 100]
print(list7)
list8 = sorted(list7)
print(list8)

# сравнение
a = [1, 2, 3]
print(a)
b = a
print(b)
b.append(77)
print(a)
print(b)
b.append(99)
print(a)
print(b)

# tuple - кортеж
# list - mutable, изменямый
# tuple - immutable, не изменямый
tuple1 = (1, 2, 3)
print(type(tuple1))
print(tuple1)
list1 = [4]
print(type(list1))
print(list1)
tuple1 = (4, 2)
print(type(tuple1))
print(tuple1)
tuple2 = ()
print(type(tuple2))
print(tuple2)
tuple2 = tuple()
print(type(tuple2))
print(tuple2)

tuple1 = (1,2,3)
#del tuple1[2]
a = tuple1[1:]
print(type(a))
print(a)
tuple1 = 4, 5, 6
print(type(tuple1))
print(tuple1)
print(len(tuple1))
fio_tuple = ('john', 'Doe', '2000', 'male')
# a, b = myfunction(fio_tuple)
a = 10
b = 20
# v1
print('a', a)
print('b', b)
c = a
a = b
b = c
print('a', a)
print('b', b)
# v2 - with tuple
a,b = b,a
print('a', a)
print('b', b)
a = ('a', 'b', 'c')
print(a)
a1, *a2, = a
print(a1, a2)