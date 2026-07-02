# There are various paradigms in programming world such as procedural functional and object oriented. 
#  Lets look at functional/procedural first

# suppose we have some information of students

def main():
    name , house = get_student();
    print(f'{name} is from {house}')

def get_student():
    return (input('Enter the name : '), input('Enter the house : '))

if __name__ == '__main__':
    main()

# Here we are returning multiple values (white-lie) --> we are actually returning a single value which is a tuple 
# tuple is the same as list but it is immutable we cannot index intro it and change something.

# we can also return a list or a dictionary (if we want to change something) 

def main():
    name , house = get_student()
    if(name == 'Padma'):
        house = 'Ravenclaw'
    print(f'{name} is from {house}')

def get_student():
    return [input('Enter the name : '), input('Enter the house : ')]

if __name__ == '__main__':
    main()

# It would be a lot better if we could just say "student is a data type it has name and house"
# Object oriented programming allows us to do just that via classes which are blueprints or molds for an object.

# Eg car is a class and it has wheels, doors, transmission etc.
# ... is a placeholder for a class

class Student():
    def __init__(self, name, house):
        self.name = name;
        self.house = house;


def get_stu():
    student = Student('Abdullah', 'dfskjdskjkl')
    student.name = input('Enter the name : ')
    student.house = input('Enter the house : ')
    return student

student = get_stu()
print(f'the student object has {student.name} + {student.house}')

# The student in this example is the object or instance
# The name and the house are instance variables or attributes

# We can use the __init__(self,name,house) --> this is an init dunder method that is used to initialize instance variables (this is also known as the constructor)

# always use self as it tells init about the current object calling the init

# __new__ --> creates the object in memory, __init__ initializes it.

st = Student('abdullah','xyz')
print(st.name,st.house)

# raise exceptions if one of the parameters are missing in the init

class Test:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError('Missing the name...')
        if house not in ['Gryffindor','Slytherin','Ravenclaw','Hufflepuff']:
            raise ValueError('Invalid house name...')
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f'{self.name} is from {self.house} and has a patronus {self.patronus}'

    def get_st_test(self):
        try:
            return (self.name, self.house)
        except ValueError:
            pass
    def charm(self):
        print('Expecto Patronum!!!')
        match self.patronus:
            case 'Stag':
                print('🦌')
            case 'Jack Russel Terrier':
                print('🐕')
            case 'Otter':
                print('🦦')
            case _:
                print('🏒')
t1 = Test('Harry','Gryffindor','Stag')
print(t1.get_st_test())

# If we want to make an argument optional, we can assign it a default value of None and we can also use our custom errors

# Printing the object directly gives us access to the object's memory, however we can use the __str__(self) method to return a string when an object is printed.

# use the __str__ method to print the info in a string format

print(t1)
t1.charm()

# Add another property called 'patronus' and a method called charm which prints the patronus.

# Notice that we are adding validation but we can still circumvent that using student.house = 'whatever', even after adding the correct house in the __init__ method. To solve this problem we use properties


# THE REST OF THE CODE IS IN THE SECOND FILE

