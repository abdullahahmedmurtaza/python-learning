def main():
    name = input('Enter your name : ')
    print(hello(name))

def hello(name = 'World'):
    return f'Hello, {name}'

if(__name__ == '__main__'):
    main()