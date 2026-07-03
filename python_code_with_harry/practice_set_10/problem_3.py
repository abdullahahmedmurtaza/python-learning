class Test:
    a = 'a'

    def give_class_attribute(self):
        print(Test.a)


test_obj = Test()
test_obj.a = 'o'

print('Class Attribute : ')
test_obj.give_class_attribute()

print(f'Instance attribute is : {test_obj.a}')

#Key point : Class attribute cannot be changed, it is fixed. The instance attribute takes precedence over the class attribute
