class Employee:
    company = 'ITC'

    def show_info(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        print(f'The employee name is: {self.name}\n the employee age is : {self.age}\n the employee salary is : {self.salary}')

class Coder:
    languages = 'JS,Java,Rust'

    def show_languages(self):
        print(f'The languages are: {self.languages}')



class Programmer(Employee,Coder):
    language = 'JS'
    company = 'avanza'

e = Employee()
p = Programmer()


e.show_info('abdullah', '21','350000')
print(p.language)

print(e.company, p.company)
p.show_languages()


#The programmer class inherits methods and properties from both Employee and coder and this is known as multiple inheritance

