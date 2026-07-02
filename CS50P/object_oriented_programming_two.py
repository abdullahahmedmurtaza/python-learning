# @property --> @ is a decorator which is a method that changes the behavior of some other method

# In order to prevent coders from circumventing the validation checks in the class we use getters and setters to set the instance variables. These are methods that prevent (somewhat) direct access to the variable.
# 1. the name of the setter and getter must be the same as the attribute.
  
# 2. the getter uses --> @property and the setter uses @property_name.setter

# 3. (self, new_value) for setter and only (self) for getter

# 4. Avoid naming collisions by assigning self._propertyname in the __init__ method. 

# 5. It is still possible to circumvent this using _propertyname but there is no proper way to prevent this in python, it is just an honor code --> DO NOT TOUCH ANYTHING WITH _ or __.

# 6. ALWAYS perform the error checks in one place i.e the setter.


# ------------------------------------------------------------------

# Clean Code with all best practices implemented

# ------------------------------------------------------------------

class Student:
    def __init__(self,name,house):
        self._name = name
        self._house = house
    @property
    def house(self):
        return self._house
    @house.setter
    def house(self,house):
        if house not in ['Gryffindor','Slytherin','Ravenclaw','Hufflepuff']:
            raise ValueError('Invalid House...')
        self._house = house
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError('Missing Name...')
        self._name = name
    def __str__(self):
        return f'{self.name} is from {self.house}'
        
st = Student('Harry','Gryffindor')
print(st)

# We have been using classes all along. Everything in python is a class
# When we use int(x,base=10) --> we were creating an int object in memory.
# Similarly for string we used methods like split(), strip()
# Similarly for list([iterable]) any iterable can be converted to a list

# See type(value) to check the type of anything

# Sometimes it is needed to not associate the methods of a class with the object but with the class itself

# for this we have another decorator @classmethod --> doesn't need self but knows to class to which it belongs.

# Implement a sorting hat that randomly assigns a student to a house
# class method needs a cls in the arguments.

import random
class Hat:
    houses = ['Gryffindor','Slytherin','Ravenclaw','Hufflepuff']
    @classmethod
    def sort(cls,name):
        return f'{name} is assigned to {random.choice(cls.houses)}'

print(Hat.sort('Ahmed'))

# Easy because we do not need to initialize an object everytime we need to sort
# This example doesn't particularly need a class but we will use one when the code gets complicated in terms of relationship of methods.

# There are other methods as well like @static methods

# OOP allows us to arrange classes in hierarchical manner as well. This concept is known as inheritance.

class Wizard:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        ...
class Professor:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

# Every student and professor and student is a wizard but we are increasing redundancy in our code by taking name both times.

# We can inherit the professor and student from the Wizard class

class Wizard: 
    def __init__(self,name):
        if not name:
            raise ValueError('Missing Name...')
        self.name = name
    ...
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    ...
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    ...

wizard = Wizard('Albus')
student = Student('Harry','Gryffindor')
professor = Professor('Severus','Defense Against the Dark Arts')

# In python, the exceptions are also arranged hierarchically e.g ValueError inherits Exception which inherits Base Exception because certain exceptions have similar functionality.

