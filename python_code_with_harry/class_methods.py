# class method is a way to access a class directly in a method
# it is basically used to override the natural behaviour of the instance attribute taking precedence over the class atrribute we just have to use 'cls' instead of 'self'


class Test:
    attribute = 0

    
    # shows the instance attribute
    # def show_attribute(self):
    #     print(f'The class attribute is : {self.attribute}')

    @classmethod
    def show_attribute(cls):
        print(f'The class attribute is : {cls.attribute}')
    

t_obj = Test()
t_obj.attribute = 1

t_obj.show_attribute()

#self --> the object on which the method is running
# cls --> the class to which the object belongs on which the method is running



