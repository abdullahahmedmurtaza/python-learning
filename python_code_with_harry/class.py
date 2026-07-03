#OOP is a programming paradigm that basically allows us to implement the DRY principle (DO NOT REPEAT YOURSELF)

#We deal with classes and objects here, class is a blueprint object is the actual implemented thing blank form --> class, filled form --> object


#Simple way to create a class and an object

class Student:
    department = 'BSCS' # Class attribute
    batch = '24F'

st1 = Student()
st1.name = 'Abdullah' # Instance attribute

print(st1.name, st1.batch, st1.department)

#Class defines a template only the actual memory is allocated when we create (instantiate) and object
#Objects can invoke the methods and properties in available to it without showing the actual implementation details to the user (Abstraction and Encapsulation)

# In order to model any problem in OOP we have to identify the following Noun -- Class Name, Adjectives -- Attributes, Verbs -- Methods (functions)

# Attributes can belong to the class and also to the object as well, they are called class attributes and instance attributes respectively.

# Instance attributes take precedence over class attributes during assignment and retireval, important point (see instance_vs_class_attributes.py)
