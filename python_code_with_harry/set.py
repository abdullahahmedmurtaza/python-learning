#a set in python is the same as a mathematical set, it cannot contain duplicate values and the syntax for initializing an empty set is e=set() and not {} --> this means empty dictionary, various datatypes can also be added

s_0 = {1,2,33,33,33,43,21,76,55,76,'YO'}

s = set()

#add method adds in the front
s.add('Hello')
s.add('World') 


print(s)
print(s_0)

#unordered, unindexed, no duplicate values, no way to change existing items in sets expect removing and inserting

s_0.remove(1)# removes the value from the set
print(s_0)

#pop removes a random value from a set not used 

#all set operations can be performed, same as mathematics and issubset / issuperset is also used
