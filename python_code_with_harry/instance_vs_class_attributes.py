# During setting and getting the instance attributes take preference over class attributes

class Test:
    attr1 = 'Hey I am 1st attribute'
    attr2 = 'Hey I am 2nd attribute'

test_obj1 = Test()

print(test_obj1.attr1,test_obj1.attr2)

test_obj1.attr1 = 'I am instance attribute'

print(test_obj1.attr1)

# see self.py