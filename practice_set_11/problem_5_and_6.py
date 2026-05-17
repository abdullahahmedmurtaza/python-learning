class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,other):
        return Vector(self.x+other.x, self.y+other.y, self.z + other.z)
    def __mul__(self,other):
        return Vector(self.x*other.x, self.y*other.y, self.z*other.z)
    
    def __str__(self):
        return f'{self.x}i + {self.y}j + {self.z}k'
    
v1 = Vector(2,3,4)
v2 = Vector(5,4,9)

print(v1+v2)
print(v1*v2)
        