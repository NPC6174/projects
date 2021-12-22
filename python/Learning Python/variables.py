#
# Example file for variables
#

# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring a variable works
myint = "abc"
print(myint)

# to access a member of a sequence type, use [] using a zero-based index value
print(mylist[2])
print(mytuple[1])

# use slices to get parts of a sequence --> '[1:5]' will output all parts starting at index value 1 and ending at index value 5
print(mylist[1:5])
# slices can also use a step value which is how many values to skip over --> '[1:5:2]' the third colon value is the step value
print(mylist[1:5:2])
# you can use slices to reverse a sequence
print(mylist[::-1])

# dictionaries are accessed via keys --> 'mydict = {"one" : 1, "two" : 2}' the values "one" & "two" are the keys for the values '1' & '2' respectively
print(mydict["one"])

# ERROR variable of different types cannot be combined
# print("string type" + 123) # Python cannot combine a string and a number in this case
print("string type" + str(123)) # By converting the integer '123' into a 'str()' type it is combining two strings

# Gloabl vs. local variables in functions
def someFunction():
    global mystr
    mystr = "def"
    print(mystr)

someFunction()
print(mystr)

del mystr
print(mystr)