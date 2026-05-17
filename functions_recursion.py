#functions are used to increase code modularity and reusability. and also to put repeatable tasks in a function and call the function when the task is to be performed to keep track of what part of code is doing what. Same things in function call and function definition

def avg(n1,n2,n3):
    return (n1+n2+n3)/3
print(avg(2,2,2))


#methods can also have default arguments

def greet(name,ending='Good morning'):
    print(f'{ending} {name}')

greet('Abdullah')

#built in function already present in python without imports, all the functions above are user-defined

#arguments and parameters are the same thing with different perspectives, at the time of definition --> parameters, at the time of calling --> arguments

#the returned value can be stored in a variable but unlike js, the entire function cannot be stored in a variable


#recursion is a phenomenon in which a function calls itself until a base-case is reached

def fact(n):
    if(n==1 or n==0):
        return 1
    return n * fact(n-1)

print(fact(3))

#most direct way to implement an algorithm
