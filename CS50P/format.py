# Suppose we have a form on Google Forms or M365. 
# We have to assume that the user does not write the data in the form that we require it. 
# We can clean the data manually but it is not a fun way to do things, instead we can write code.

# Consider a user's name

# Some people might write their names as lastname, firstname

name = input('Enter your name : ').strip()
if ',' in name:
    last, first = name.split(', ')
    name = f'{first} {last}'
print(f'hello, {name}')

# There is still a problem if the user has a comma in their name, or what if there is no space after the comma? the condition checks for ', ' --> we get a ValueError

import re

# Search can also return information like whether or not a group was matched.

if res := re.search(r'^(.+), *(.+)$', name):
    name = f'{res.group(2) +" "+ res.group(1)}'
print(name)

# Use walrus operator := to assign a value to a variable and ask a boolean question about it.