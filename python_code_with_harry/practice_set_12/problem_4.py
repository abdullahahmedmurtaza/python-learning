a = int(input('Enter a : '))
b = int(input('Enter b : '))

try :
    res = a/b
    print(res)
except ZeroDivisionError:
    print('Infinity')