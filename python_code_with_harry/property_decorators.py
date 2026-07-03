#Property decorator is used to make a method behave like a property or attribute.

#It is also used to set two different instance attribute from a single instance attribute

#property decorators combined with setters can help us make changes to the class without affecting the way the class is being implemented by other people.


#This example mainly demonstrates how to set multiple instace attributes by using (setting) only one instance attribute

class Employee:
    @property
    def name(self):
        return f'{self.fname} {self.lname}'
    @name.setter
    def name(self, value):
        self.fname = value.split(' ')[0]
        self.lname = value.split(' ')[1]
e = Employee()
e.name = 'Abdullah Ahmed'

print(e.lname)






# More practice for the property decorators with getters and setters

class Test:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f'{first}.{last}@email.com'
    
    def fullname(self):
        return f'{self.first} {self.last}'
    

e = Test('Abdullah', 'Ahmed')

print(e.first)

e.first = 'Jim'

print(e.first)

print(e.email)


print(e.fullname())


# Why is is it not adding Jim in the email????????




#The email is not updated because it is only created once inside the constructor now, to fix this we CAN create a method inside the class for the email like we have for the fullname. BUT then everyone using our class will have to change their code to a method call with parentheses rather than just an attribute, --> That is where @property comes in.





# Because email is only created once inside __init__().

# When you do:

# self.email = f'{first}.{last}@email.com'

# Python stores that string permanently at object creation time.

# So after:

# e = Test('Abdullah', 'Ahmed')

# e.email becomes:

# 'Abdullah.Ahmed@email.com'

# Later, when you change:

# e.first = 'Jim'

# only first changes. The email string does not automatically rebuild itself.

# That’s why your output is still:

# Abdullah.Ahmed@email.com

# A better approach is to make email a method or a property so it updates dynamically.

# Example using @property:

# class Test:

#     def __init__(self, first, last):
#         self.first = first
#         self.last = last

#     @property
#     def email(self):
#         return f'{self.first}.{self.last}@email.com'

#     def fullname(self):
#         return f'{self.first} {self.last}'


# e = Test('Abdullah', 'Ahmed')

# print(e.email)

# e.first = 'Jim'

# print(e.email)

# Output:

# Abdullah.Ahmed@email.com
# Jim.Ahmed@email.com

# @property makes email behave like an attribute, but it recalculates every time you access it.


# deleter also works in the same way..... 
# Just set self.prop1 and self.prop2 both to None
# and while implementing use del obj_name.intance_attribute_name



