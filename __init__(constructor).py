#Important topic : in python the constructor is called the init dunder method 

#One of the way to set things instead of doing it manually is to use the init method which takes the self arguments

#Constructor is method that runs itself at instantiation


class Human:
    arms = '2'
    legs = '2'

    def __init__(self): #dunder method which is automatically called
        print('I am creating an object')

ali = Human()


#Passing attributes as arguments to the constructor is a really good practice

class Employee:
    language = 'Python'
    salary = 120000

    def __init__(self,salary,name,language):
        self.name = name
        self.language = language
        self.salary = salary

        print(name, language, salary)

emp_1 = Employee(20000, 'abdullah', 'JS')


