#
# Example file for working with functions
#

# TODO: define a function
def func1():
    print("I am a function")

# TODO: function that takes arguments
def func2(arg1, arg2):
    print(arg1," ", arg2)

# TODO: function that returns a value
def cube(x):
    return x * x * x

# TODO: function with default value for an argument
def power(num, x=1):
    result = 1;
    for i in range(x):
        result = result * num
    return result

# TODO: function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result



func1() # executes 'func1()' function

func2(10, 20)

print(cube(3)) # 'print()' must be used for 'return' functions defined

print(power(2))
print(power(2,3))

print(power(x=3, num=2)) # Python allows you to call a function with their values named regardless of order

print(multi_add(4,5,10,4))