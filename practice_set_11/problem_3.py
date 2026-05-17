#given formula is new salary = old salary + (1+increment/100)
# so the increment becomes ((new salary / old salary) -1) * 100 


class Employee:
    salary = 0
    increment = 0

    def __init__(self,salary,increment):
        self.salary = salary
        self.increment = increment

    def show(self):
        print(f'salary {self.salary}, increment {self.increment}')

    @property
    def salaryAfterIncrement(self):
        return f'Salary after increment is {self.salary + self.salary  * (self.increment/100)}'
        
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary)-1)*100

e = Employee(20000,2)
e.show()
e.salaryAfterIncrement = 280.8
print(e.salaryAfterIncrement)