class Animals:
    def __init__(self):
        print(f'Instance created! I am from class Animals')
class Pets(Animals):
    def __init__(self):
        super().__init__()
        print(f'I am Pets constructor')
class Dog(Pets):
    def __init__(self):
        super().__init__()
        print('I am constructor of Dog class')
    @staticmethod
    def bark():
        print(f'Bark!')

a = Animals()
p = Pets()
d = Dog()
d.bark()