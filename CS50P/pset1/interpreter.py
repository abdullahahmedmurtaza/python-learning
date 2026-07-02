exp = input('Enter an expression : ')
x = int(exp.split(' ')[0])
y = (exp.split(' ')[1])
z = int(exp.split(' ')[2])
match y:
    case '+':
        result = float(f'{x+z}')
    case '-':
        result = float(f'{x-z}')
    case '*':
        result = float(f'{x*z}')
    case '/':
        result = float(f'{x/z}')
    case '%':
        result = float(f'{x%z}')
    case _:
        result = 'Unsupported operation'
print(result)
