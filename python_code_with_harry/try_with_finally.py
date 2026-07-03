#Most explanations say that the finally block runs no matter what, but then why do we use it? we can also use a simple statement after that right?
# However the real usage of the finally block is in functions, because if we return from the function in the try block then the standalone statement won't run, but if we use finally it will still run after returning from the function.

#finally runs even if the function returns

try:
    a = int(input('Enter a number : '))
except Exception as e:
    print(e)
finally:
    print ('I am finally')

