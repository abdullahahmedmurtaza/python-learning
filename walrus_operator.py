# the walrus operator is used to assign the values to a variable as part of an expression, for example instead of doing this: 
# n = len([12,23,44,21,2,11,7])
# if (n>3) ----- do something
# we can do this if(n := len([1,2,3,4,5,6])) -- do something.
# The official name for this is assignment expression

if(n:=len([1,2,3,5])>3):
    print('length is greater than 3')