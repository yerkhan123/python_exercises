# simple operations on files
# "r" - read (default)
# "w" - write, start new file
# "a" - append
# "x" - create if doesn't exist
# "r+" - read/write

# read file
myfile = open("mydata.txt", "r", encoding="utf-8")
myline1 = myfile.readline()
print(myline1)
myline2 = myfile.readline()
print(myline2)
myline3 = myfile.readline()
print(myline3)
print("-"*10)
myline4 = myfile.readline()
print(type(myline4))
print("+"*10)
print(myline4)
myfile.close()

myfile = open("mydata.txt", "r")
text = myfile.read()
print(text)
myfile.close()

myfile = open("mydata.txt", "r")
for line in myfile:
    print(line.upper())
myfile.close()


myfile = open("myoutputfile.txt", "w")
myfile.write("Hello file from Python!")
myfile.close()

myfile = open("myoutputfile.txt", "a")
myfile.write("\nAno\nther additional text!")
myfile.write("\nThis is the third li\nne!")
myfile.write("\n")
myfile.write( "="*12)
myfile.write("\nabc\rdefg\thijk")
myfile.close()