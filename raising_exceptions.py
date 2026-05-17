a = int(input('Enter a number : '))
b = int(input('Enter the second number : '))
if (b==0):
    raise ZeroDivisionError('Division by zero is not allowed')
print(a/b)



# exceptions are raised for other people using our module