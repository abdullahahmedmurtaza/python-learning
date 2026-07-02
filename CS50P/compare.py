# CONDITIONALS --> ask mathematical questions then make decisions

x = int(input('Enter x : '))
y = int(input('Enter y : '))
if x<y:
    print('x is smaller than y')
if x>y:
    print('x is greater than y')
if x==y:
    print('x is equal to y')

# expressions work on booleans --> true or false.
# above approach is not good use elif to check step by step in mutually exclusive events


if x<y:
    print('x is smaller than y')
elif x>y:
    print('x is greater than y')
elif x==y:
    print('x is equal to y')

#use else as a catch-all to catch everything

if x<y:
    print('x is smaller than y')
elif x>y:
    print('x is greater than y')
else:
    print('x is equal to y')

# Conditions can be combined using or, and etc.

if(x>y or x<y):
    print("x is not equal to y")
else:
    print("x is equal to y")
# This code can be further improved

if (x==y):
    print("x is equal to y")
else:
    print("x is not equal to y")




