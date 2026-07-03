# exception handling basically means that the app does not crash due to the programmer's failure

# Crashing means that anything below the point where an error occurs is not executed 

# for example, the program required username in string but the user typed an int or a float or a boolean

# this can be handled gracefully by using the try-except block, where we TRY to do something and if it goes wrong, we catch the EXCEPTION and print the message

try:
    a = int(input('Enter a number : '))
    print(a)
except ZeroDivisionError:
    print('Yo! this is a zero division error')
except Exception as e:
    print(e)

print('After try-except')

#multiple type of exceptions can also be handled





    
