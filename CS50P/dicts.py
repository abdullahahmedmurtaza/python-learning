# Collection of key value pairs

dictionary = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Draco" : "Slytherin",
    "Ron" : "Gryffindor"
}

for student in dictionary :
    print(student, dictionary[student], sep=' --> ')

# by default for iterates over a dictionary to print keys
# keys also act as indices.

# in actual programs, we have a lot of data from databases through API's in tabular form sometimes

# In this case we use a list of dictionaries

students = [
    {
        'name' : 'Hermione',
        'house' : 'Gryffindor',
        'patronus' : 'Otter'
    },{
        'name' : 'Harry',
        'house' : 'Gryffindor',
        'patronus' : 'Stag'
    },{
        'name' : 'Ron',
        'house' : 'Gryffindor',
        'patronus' : 'Jack Russell Terrier'
    },{
        'name' : 'Draco',
        'house' : 'Slytherin',
        'patronus' : None # None is a datatype in python representing nothing
    }
]

for student in students :
    print(student['name'], student['house'], student['patronus'], sep=' | ' )

# Dictionaries make it easier to get our relevant data from the source using method (more on that later)

