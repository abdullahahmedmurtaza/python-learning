# # We have to do something repeatedly

# print('meow')
# print('meow')
# print('meow')

# #  imagine we want to print 1000 times, the code gets difficult to maintain very fast.

# # violated the DRY principle (DO NOT REPEAT YOURSELF)
# # using while loop

# count = 0
# times = int(input('Enter the number of times you want to print : '))
# while(count != times):
#     print('Meow')
#     count += 1  # updation

# # Another type of dloop in python is a for loop, Here we will see how a for loop iterates in a list

# # List is a data type in python which stores multiple values


# for i in [0,1,2]:
#     print(i)

# # poorly design, for 10000 will we put 0 - 9999?
# # use the range fuction to get a range of values
# # the range goes UPTO not THROUGH the number I input

# # For variables that we do not need, we can use _ to signify that the variable does not hold any meaning i.e we don't use it

# for i in range(5): # Goes from 0 to 4
#     print(i)

# # We only need a positive value from the user so until the user enters a positive number we have to keep prompting

# # For this we intentionally use an infinite while loop

# while True:
#     num = int(input('Enter a number : '))
#     if num > 0 : break

# print('Positive num = ',num)

# # This can be further simplified by

# print('meow\n' * num, end='')

# #  use functions to modularize the code

def main():
    meow(getNumber())
def getNumber():
    while True:
        n = int(input('Enter the number : '))
        if n > 0 : return n
def meow(n):
    print('Meow\n' * n, end='')
main()


