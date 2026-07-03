class Programmer:
    language = 'C++'
    salary = '120000'
    role = 'Junior SWE'


    #MULTIPLE CONSTRUCTORS NOT SUPPORTED

    # def __init__(self):
    #     print(f'Employee Added! \n name : {self.name} \n role : {self.role} \n language : {self.language} \n salary : {self.salary}')

    def __init__(self,name,role,language,salary):
        self.name = name
        self.role = role
        self.language = language
        self.salary = salary
        print(f'Employee Added! \n name : {name} \n role : {role} \n language : {language} \n salary : {salary}')

programmer_1 = Programmer('abdullah', 'SWE', 'JS', 300000)
programmer_2 = Programmer('ali', 'Senior SWE', 'Java', 600000)
programmer_3 = Programmer('usman', 'Operations Manager', 'Rust/C++', 500000)
programmer_4 = Programmer()




#Multiple constructors problem

# Yes. In Python, you cannot create multiple constructors with the same name like in languages such as Java or C++.

# This will not work because the second __init__ replaces the first one:

# class Test:
#     def __init__(self):
#         print("First")

#     def __init__(self, name):
#         print("Second")

# Only the last __init__ exists.

# Instead, Python uses:

# 1. Default parameter values
# class Test:
#     def __init__(self, name="Guest"):
#         self.name = name
#         print("Hello", self.name)

# Test()
# Test("Ali")

# Output:

# Hello Guest
# Hello Ali
# 2. Variable-length arguments (*args, **kwargs)

# If you want constructor-like flexibility:

# class Test:
#     def __init__(self, *args):
#         if len(args) == 0:
#             print("No arguments")
#         elif len(args) == 1:
#             print("One argument:", args[0])
#         else:
#             print("Multiple arguments:", args)

# Test()
# Test("Ali")
# Test("Ali", 20)

# So Python does not support constructor overloading directly, but default values and *args are the common alternatives.