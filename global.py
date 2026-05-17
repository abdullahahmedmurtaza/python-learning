# variables defined inside a function .are particular to that function only (local variables) and the functions defined outside are called global variables. 

# in order to change the global variable we have to use the keyword global 


a = 89
def fun():
    global a
    a = 3
    print(a)

fun()
print(a)

