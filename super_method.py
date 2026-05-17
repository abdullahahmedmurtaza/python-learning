#super method is used to call the constructor of the parent class or the super class inside the derived or the subclass

class SuperClass:
    def __init__(self):
        print('Hi! I am super constructor!')

class SubClass(SuperClass):
    
    def __init__(self):

        #always call the super constructor within the actual constructor of that class
        super().__init__() #no need to pass self here



        print('Hi! I am sub constructor')


super_obj = SuperClass()
sub_obj = SubClass()
