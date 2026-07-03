# Suppose we have a list of student names and we want to add their houses.

# The simplest way is iteration

students = [
    'Harry',
    'Hermione',
    'Ron'
]

gryffindors = []
for student in students:
    gryffindors.append({'name' : student, 'house' : 'Gryffindor'})
print(gryffindors)

# The next simplest way is using a list comprehension

# The first step is to find out WHAT to add exactly e.g here we want to add a dictionary
# We take the student's name from our students list

gryffindors_2 = [{'name' : student, 'house': 'Gryffindor'} for student in students ]
print(gryffindors_2)


# Here we are still getting a list but what if we want a dictionary where the names are the student names and the house is gryffindor. No need for a list

dictionary = {student : 'Gryffindor' for student in students}
              #Key       # Value
# Key is extracted from the loop after it.
print(dictionary)


# Suppose we want to print the rank or serial number before each student as well, 
# We can do that using a simple for loop and an iterator but it is again not succint
# Python provides us with a function called enumerate(iterable, start=0) --> give it an iterable, tell it where to start from, it will gove both the number and the value, which can be unpacked.

for i, val in enumerate(students,1):
    print(i,val)