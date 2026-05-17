# In other languages like c++ and Java we use the data type with a variable like int a = 1,  String str = "Java" etc, but in python we have not done this till now.
# Python does however provide us with this feature where we can define the types and access all the relevant methods

# The syntax varies a little bit in the case of variables and the return type of the functions

# Practice and experimentation is given below

a : int = 1
print(a)

def sum(a:int,b:int) -> int:
    return a+b

# This is a best practice as it allows you as well as other programmers to understand the code by observing the data types at a glance because it provides type hints

print(sum(12,13))


# Advanced Type Hints, Python provides advanced type hints when we use typing module to import List, Tuple, Dict, Union 

from typing import List, Tuple, Dict, Union

l : List[int] = [1,2,3,4,5]
t : Tuple[str] = ('Ali','Abdullah','Pritam','Muzammil','Huzaifa')
d : Dict[str,int] = {'ali':90, 'ahmed':75}

# Union type is used for variables that can hold multiple types

i : Union[str,int] = 12

print(i)

i = 'stringgggg'

print(i)