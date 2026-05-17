# Inheritance is a really important concept in OOP where one class can have the propeerties and methods of another class and also have some properties and methods of its own

# If there are 10 classes and we copy-paste all the methods, it is not going to be a good approach instead we can inherit the methods and make changes once in the parent class method (Modularity++)  -- keeps methods consistent within classes

# Here is how we inherit the classes:

class Employee:
    company = 'ITC'

    def show_info(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        print(f'The employee name is: {self.name}\n the employee age is : {self.age}\n the employee salary is : {self.salary}')

class Programmer(Employee):
    language = 'JS'
    company = 'avanza'

e = Employee()
p = Programmer()


e.show_info('abdullah', '21','350000')
print(p.language)

print(e.company, p.company)


# Technical Terms : Base class -- Parent Class, Derived Class -- Child Class 
# Single Inheritance : Parent --> Child