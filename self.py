# This file explains the self attribute using a method defined in a class


# WRONG CODE FOR EXAMPLE



# class Employee:
#     language = 'Python'
#     salary = '120000'
    
#     def getInfo():
#         print(f'The language is {language}, The salary is {salary}')

# abdullah = Employee()

# abdullah.getInfo()


 
 #-------------------------------------------------------------------------------------------------------------------------------------------------------------


#This gives an error (TypeError: Employee.getInfo() takes 0 positional arguments but 1 was given), but why? we didn't give any arguments

# This is because the call is converted to this Employee.getInfo(abdullah) implicitly

#To solve this we use the 'self' keyword/parameter in the method definition which tells Python 'Hey, this is the object on which the method is called' use this to accept the positional argument


#CORRECT CODE 

class Employee:
    salary = 120000
    language = 'Python'

    def get_info(self):
        print(f'The salary is {self.salary}, The language is {self.language}')
    
    @staticmethod #this decorator indicates that it doesn't need self 
    def greet():
        print('Good Morning')

abdullah = Employee()
abdullah.greet() #marked as a static method (explained later)
abdullah.get_info() #actually Employee.get_info(abdullah)

#The code runs perfectly now.

#Key point : accept the object you are calling the method on, and instance attributes take recedence over class attributes

# in the greet method we are passing and entire object just for greeting, I doesn't even use anything from the object. There is a better way

# we can just mark the greet as a @staticmethod which doesn't need an argument (This is called a decorator)