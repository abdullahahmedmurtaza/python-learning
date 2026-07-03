class Test:
    a = 'a'

    def give_class_attribute(self):
        print(Test.a)

    @staticmethod
    def greet(name = 'John'):
        print(f'Hello! {name}')
        
test_obj = Test()
test_obj.a = 'o'

print('Class Attribute : ')
test_obj.give_class_attribute()

print(f'Instance attribute is : {test_obj.a}')

Test.greet('Abdullah')