# Operator overloading means to make an operator behave differently by defining our own rules, e.g + means something else for ints and something else while concatenating str.

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    def __str__(self):
        return f'{self.galleons}, {self.sickles}, {self.knuts}'
# Suppose we want to add the vaults of two people then we have to define the what addition means for our class vault --> this is done using the __add__(self, other) method --> self means left side operand, other means right side operand

    def __add__(self, other):
        return Vault((self.galleons+other.galleons),(self.sickles+other.sickles),(self.knuts+other.knuts))
    

potter = Vault(25,50,100)
weasley = Vault(87,12,75)

print(potter)
print(weasley)

# Total Vault
print(potter+weasley)

# More operators can also be overloaded --> use special methods documentation.

# Always use OOP to model real-world entities as problems get more and more complex
