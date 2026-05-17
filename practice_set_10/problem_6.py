#changing the self param to slf or something else

class Test:
    attr_1 = 1
    attr_2 = 2

    def __init__(slf):
        print('Hi! I am init, new instance created')
    
obj_1 = Test()

#The code still works because 'self' is just a best practice to catch the instance being passed as Test.__init__(obj_1)

