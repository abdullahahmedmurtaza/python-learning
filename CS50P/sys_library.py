# We can give input to the program right from the command line which is known as command-line arguments (not only in python but in other programming languages as well). 

# for this we need the sys (short for system) module

import sys

# sys.argv is a variable that has a list of all the arguments we provide from the command line, the [0] is the name of ther program

# print('Hi! My name is',sys.argv[1])

# We can try to get the input from the user i.e their name and we can also except errors (particularly IndexError).

# Or we can use if elif else to check for the things we are worried about

# if(len(sys.argv) > 2):
#     print('too many arguments')
# elif(len(sys.argv) < 2):
#     print('too few arguments')
# else:
#     print(f'Hi! My name is {sys.argv[1]}')
# Generally it is a good practice to keep the actual code separate from the error checking but then we get an IndexError so, we use sys.exit() to exit the program if there is a bug

if(len(sys.argv) > 2):
    sys.exit('too many arguments')
elif(len(sys.argv) < 2):
    sys.exit('too few arguments')

print(f'Hi! My name is {sys.argv[1]}')


