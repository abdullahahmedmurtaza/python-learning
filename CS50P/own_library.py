import sys
def hello(name = 'World'):
    print(f'Hello, {name}')
def goodbye(name = 'World'):
    print(f'Goodbye, {name}')

def main(funcName):
    hello()
    goodbye()



# This means only execute the main if I run this file otherwise if I import it do not run it.
if(__name__ == '__main__'):
    main()