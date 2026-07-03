#For this problem the length of the vector must be variable and stored in the form of a list

class Vector:
    def __init__(self,l):
        self.l = l

    def __len__(self):
        return len(self.l)
        


v1 = Vector([2,3,4,5])

print(v1.__len__())

  