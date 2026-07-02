def main():
    num = int(input("Enter the number : "))
    print(isEven(num))

# def isEven(n):
#     return True if n % 2 == 0 else False

# We can also return a boolean expression

def isEven(n):
    return n % 2 == 0

main()
