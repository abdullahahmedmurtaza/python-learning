#  Exceptions in code are errors that indicate something is wrong with our program

# e.g intentionally missing a closing quote
# print('Hello World)
      
# gives SyntaxError

# Some problems in our code cannot be resolved regardless of how many times we rerun it, like the Syntax Error

# We also have errors that arise at runtime called runtime errors.
# We have to write some code defensively to prevent this.
# e.g user mistyping different things

# x = int(input('What is x : '))
# print(x)

# Gives ValueError if the user gives a string
# get comfortable reading error messages.


# If we wish to catch errors (SyntaxError, ValueError), we need something like 'try' --> try to do something, 'except' --> except if anything goes wrong do this


try:
    x = int(input('What is x : '))
    print(x)
except ValueError:
    print('Please enter an integer...')

# Contradictory advice : Generally not a good practice to handle everything in an except block (always mention the type of errors), but if we do not know the type of errors we can just assume if anything goes wrong do this. 

# Sometimes the documentation DOES tell us exactly what could going wrong so....

# Keep the try block small by including only those things which can actually raise an error. shift things down

# try:
#     y = int(input('Give me something else : '))
# except ValueError:
#     print('Give an integer please...')
# print(f'y is : {y}')

# Now if we give a str it gives a NameError y is not defined
# Scoping is not the problem here.

# The ValueError is occuring when we input so the literal does not get copied to the variable and as a result y becomes undefined
# To fix this we can use 'else' with try-except as well. Because it is a catch-all AFTER the try-except.

try:
    y = int(input('Give me something else : '))
except ValueError:
    print('Give an integer please...')
else: 
    print(f'y is : {y}')

# How to reprompt the user for an int

# def getInt():
#     while True:
#         try:
#             a = int(input('Enter the number : '))
#         except ValueError:
#             print('Please enter an int.')
#         else :
#             return a


# Further refinement

def getInt():
    while True:
        try:
            return int(input('Enter the number : '))
        except ValueError:
            pass
            # print('Please enter an int.')
        # else :
        #     return a


def main():
    e = getInt()
    print(e)
main()

# The pass keyword can also be used if we are trying to catch an error and not do anything with it (just reprompting)
# The pythonic way of doing things is trying and catching things

# Try to keep a prompt in a variable and pass it to another function as a parameter to use in the input(). Makes the code a bit more dynamic and user-friendly

# 'raise' keyword can also be used to raise errors delibrately.
# More on 'raise' later

        

