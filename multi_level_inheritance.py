# Class 1 --> Class 2 --> Class 3
# This is called multilevel inheritance


class Employee:
    a = 0
class Programmer(Employee):
    b = 12
class Coder(Programmer):
    c=14

o = Employee()
print(o.a)

o = Coder()
print(o.a,o.b,o.c)