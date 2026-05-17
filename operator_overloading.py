# by default everything is a class in python e.g class 'int', class 'tuple', class 'list' so, the operations + - * / // must be defined for that class which we do so by operator overloading. Consider the following example.

class Number:
    def __init__(self,n):
        self.n = n

    def __add__(self,num):
        return self.n + num.n
    
    def __sub__(self,num):
        return self.n - num.n
    
    def __mult__(self,num):
        return self.n * num.n
    
    def __div__(self,num):
        return self.n / num.n
    
    def __floordiv__(self,num):
        return self.n // num.n
    
a = Number(1)
b = Number(2)

print(a+b) #Error --> TypeError: unsupported operand type(s) for +: 'Number' and 'Number' 


# To fix this we can define dunder methods like __add__() __sub__() etc


# some other dunder methods are __str__() --> decides what happens upon calling str(obj)

#__len__() used to decide what happens when calling len(obj)