class Calculator:
    @staticmethod
    def find_square(n):
        return n**2
    @staticmethod
    def find_cube(n):
        return n**3
    @staticmethod
    def find_square_root(n):
        return n**(1/2)
    

#static methods must be called with the class name
    
print(Calculator.find_square(2))
print(Calculator.find_cube(3))
print(Calculator.find_square_root(16))