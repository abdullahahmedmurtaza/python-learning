# We have seen unpacking briefly --> taking something out of a list or a dict and putting it immediately in variables.

# Now it is time to use unpacking more powerfully

def total(galleons, sickles, knuts):
    return (galleons*17+sickles)*29+knuts
coins = [25,66,7]
# The list, however, must be controlled in order to ensure the correct calculation
print(total(*coins),'Knuts')

# the * symbol allows us to take out the values from a list and pass them one-by-one


print(*coins)

# To avoid the problem of remembering positional arguments, we can used named arguments or named parameters.

# We can also do this

print(total(galleons=25,sickles=66,knuts=7))

# This syntax reminds us a little bit of dictionaries in python.

coins_dict = {'galleons':25,'sickles':66,'knuts':7}

# Python allows us to unpack dicts as well

print(total(**coins_dict))

# functions can have variate arguments, so if we do not know how many positional, or named arguments we want to pass, we can do this
# kwargs --> keyword arguments

def test_func(*args, **kwargs):
    print('Positional :',args) # --> tuple
    print('Named :',kwargs) # --> dict

test_func(45,55,6)
test_func(45,55,6,7)
test_func(45,55,6,76,88,91,23,66)
test_func(45,55,6,76,88,91,23,66,kwarg1 = 'Yo I am kwarg 1',kwarg2 = 'Yo I am kwarg 2')

# The same thing is how print is implmeneted in the official python docs

# print(*objects, sep='\n, ...) --> might contain a for-loop to iterate over the objects and print them

