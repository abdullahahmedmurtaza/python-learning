# design bricks from mario

print('#')
print('#')
print('#')

def makeBrick(n):
    while (n>0):
        print('#'*3,)
        n-=1


# For a much more complex square printing task

def printSquare(n):
    for i in range(n):
        printBrick(n)
        print()

def printBrick(n):
    print('#'*n,end='')

def printRow(n):
    print(n*'?')

def main():
    num = int(input('Enter the height of brick you want'))
    # makeBrick(num)

    # Printing squares
    printSquare(num)

    printRow(num)

main()



