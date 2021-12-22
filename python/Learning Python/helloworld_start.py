#
# Example file for HelloWorld
#

# Print "Hello World!" and input for user to enter name
print("Hello World!")
name = input('What is your name? ')
print("Nice to meet you", name)

# Define a function that will run same code as above with check for backtrace
def main():
    print("Hello World!")
    name = input('What is your name? ')
    print("Nice to meet you", name)

if __name__ == "__main__":
    main()