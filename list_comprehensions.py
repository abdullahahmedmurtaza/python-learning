# list comprehension is a way to create a list from another list in a very elegant manner

# consider we want an entire list squared

l = [2,4,6,8,10]

# l_squared = []

# for i in l:
#     l_squared.append(i*i)

# print(l_squared)


# there is a simpler way to do this using list comprehensions

square_list =  [i*i for i in l] # runs i*i for every item in list
print(square_list)