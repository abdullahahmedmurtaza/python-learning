# There is another data type in python called set.

# Suppose we have a list of students as dicts and we want to get the houses from it while avoiding duplicates

# Difficult way
# -------------

students = [
    {'name':'Harry',
     'patronus' : 'Stag',
     'house' : 'Gryffindor'
     },
    {'name':'Hermione',
     'patronus' : 'Otter',
     'house' : 'Gryffindor'
     },
    {'name':'Padma',
     'patronus' : None,
     'house' : 'Ravenclaw'
     },
    {'name':'Draco',
     'patronus' : None,
     'house' : 'Slytherin'
     }
]

houses  = list()
for student in students:
    if student['house'] not in houses:
        houses.append(student['house'])

print(houses)

# Easy way 
#---------

houses_set = set()
for student in students:
    houses_set.add(student['house'])
print(houses_set)

# Set is unordered.
