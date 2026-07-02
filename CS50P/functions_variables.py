# x = float(input("Enter x : "))
# y = float(input("Enter y : "))

# print(f"{(x+y):,}")

# # round can also be used and the string can also be formatted upto two decimal places

# print(round(x+y,2))
# print(f"{(x+y):.2f}")

# # function

# name = input('Enter Your Name')
# def hello(name='World'): # default value
#     return f"Hello {name}"
# print(hello())

# python wants code line by ine func must be defined before using it, but then we would write code in reverse so to solve this use def main():

def main():
    name = input('Enter Your Name')
    hello()

def hello(): # default value
    print("Hello",name)

main()

# The above example illustrates scoping. (variable only exists in the context of its definition)

