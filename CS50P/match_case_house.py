# Consider this scenario

name = input("Enter the name : ")
# if(name == 'Harry'):
#     print('Gryffindor')
# elif(name == 'Hermione'):
#     print('Gryffindor')
# elif(name == 'Ron'):
#     print('Gryffindor')
# elif(name == 'Draco'):
#     print('Slytherin')
# else:
#     print('Who?')

# Can be optimized further using or keyword of harry hermione and ron

# For scenarios like this we use match
# keep the catch all as default, the syntax is '_'


match name:
    case 'Harry' | 'Hermione' | 'Ron':
        print('Gryffindor')
    case 'Draco':
        print('Slytherin')
    case _:
        print('Who?')

# Conditions can also be simplified here but instead of or we are going to use '|'. No need for break statement.