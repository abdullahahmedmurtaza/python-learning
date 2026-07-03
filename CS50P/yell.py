# Convert lowercase to uppercase using functional programming. 
# Here, we will look at map

def main():
    # print(yell('this is cs50'))


    # words = ['this','is','cs50']
    # print(*yell(words))

    # print(*yell('this','is','cs50p'))

    print(*yell_2('this','is','cs50'))

# def yell(user_str: str) -> str:
#     return user_str.upper()

# What if we want to pass multiple words, like a list of words or like in print; words separated by commas?

# For multiple args we use *args


# def yell(words) -> list:
#     uppercase = []
#     for word in words:
#         uppercase.append(word.upper())
#     return uppercase


# We do not want an output like this where we have a returned list so we can modify it further. (unpacking)

def yell(*words) -> list:
    uppercase = []
    for word in words:
        # print(word)
        uppercase.append(word.upper())
    return uppercase


# map allows us to apply some function to every element of a sequence like a list. Syntax --> map(function,iterable)

def yell_2(*words):
    uppercased = []
    uppercased.append(map(str.upper,words))
    return uppercased

# In the docs the method is called str.upper() --> do not call the method, just pass the reference.



# We can also use something called list comprehension which allows us to pass an expression to the list as follows -> method loop conditional


def yell_2(*words):
    uppercased = [word.upper() for word in words]
    return uppercased

# Similarly suppose we have to filter something out on the basis of a condition

students = [
    {'name' : 'Harry', 'house' : 'Gryffindor', 'patronus' : 'Stag'},
    {'name' : 'Hermione', 'house' : 'Gryffindor', 'patronus' : 'Otter'},
    {'name' : 'Ron', 'house' : 'Gryffindor', 'patronus' : 'Jack Russell Terrier'},
    {'name' : 'Draco', 'house' : 'Slytherin', 'patronus' : None},
]

gryffindor_students = [
    student['name'] for student in students if student['house'] == 'Gryffindor' 
    ]

print(gryffindor_students)


# Similarly there is a function called filter that is similar to map but uses a more functional approach as compared to list comprehensions

# It needs two things --> 1.A function that returns a boolean | 2. A list

gryffindors_2 = filter(lambda s: s['house'] == 'Gryffindor',students)
for gr in gryffindors_2:
    print(gr['name'])


if __name__ == '__main__':
    main()

