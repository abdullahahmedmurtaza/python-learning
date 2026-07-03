# else block is only executed when the try block is completed successfully

# if the try block fails, the else block will not be executed, and the app crashes


try:
    a = int(input('Enter a number : '))
except Exception as e:
    print(e)
else: 
    print('I am inside else block')
