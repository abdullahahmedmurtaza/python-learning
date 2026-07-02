# This file is going to help us understand the global and local variables in python

# A global variable is the one defined outside the function while the local variable is inside however, if we wish to access the global variable inside a function, we have to use the 'global' keyword

# We can read the global variable but not change it

# Local variables shadow global ones

balance = 0;

def main():
    print('Balance :',balance)
    print(deposit(50))
    print(withdraw(10))

def deposit(n):
    global balance # tells python to edit the global variable
    balance += n
    return balance
def withdraw(n):
    global balance
    balance -= n
    return balance

if __name__ == '__main__':
    main()


# This is suitable for small scripts but we can use oop to make it better

class Account:
    def __init__(self,balance):
        self._balance = balance

    @property    
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self,new):
        self._balance = new;

    def deposit(self,n):
        self.balance += n
    def withdraw(self,n):
        self.balance -= n

acc = Account(60)
acc.deposit(40)
acc.withdraw(30)
print(acc.balance)

# Try to use global variables sparingly
# global variables are local to a module

    




