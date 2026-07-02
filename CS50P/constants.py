# Constants are based purely on the honor system --> no pythonic implementation

# We use a best practice to put it at the top and in all uppercase

PI = 3.14
print(PI)

# PI = 3.1111111 # possible but not recommended 

# They can also exist within a class
class Cat:  
    MEOW = 3
    def meow(self):
        for _ in range(Cat.MEOW):
            print('meow')
cat = Cat()
cat.meow()