from functools import reduce


l = [1,2,3,4,5,6]

square = lambda x:x*x

# Map method performs a method for each item in a list, IT RETURNS A MAP OBJECT SO IT IS IMPORTANT TO CONVERT IT INTO LIST
square_l = map(square,l)
print(list(square_l))

# Filter Example

def even(n):
    if(n%2 == 0):
        return True
    return False

even_l = filter(even,l)

print(list(even_l))


# Reduce Example

def sum(a,b):
    return a+b

print(reduce(sum,l))

# reduce() needs to be imported from functools in python

