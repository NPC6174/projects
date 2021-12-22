#
# Palindrome Challenge
# Build a program that accepts a string from the user and quits when the user types the word exit.
# Otherwise the program is going to take the input string and determine if it is the same both forward and backward.
# The program should ignore spaces and punctuation characters and print the result indicating whether the string is a palindrome.
#

def is_palindrome(teststr):
    # use the slice trick to reverse the string
    if teststr == teststr[::-1]:
        return True
    return False

run = True
while (run):
    teststr = input("Enter string to test for palindrome or 'exit':")

    # If the user types "exit" then quit the program
    if teststr == "exit":
        run == False
        break

    # convert the string to all lower case
    teststr = teststr.lower()

    # strip all the spaces and punctuation from the string
    newstr = ""
    for x in teststr:
        if x.isalnum():
            newstr += x
    
    print("Palindrome test:", is_palindrome(newstr))