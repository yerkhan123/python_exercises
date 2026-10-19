mystring = input("input a number: ")

try:
    mynumber = int(mystring)
except ValueError as e:
    print("You entered not a number")
    exit(-10)
except(ErrorA, ErrorB):
    ...
except SomeError as e:
    ... 
except:
    ...
else:
    ...
finally:
    ...


try:
    ...
except:
    ...

print(mynumber)