# we need data structures that are containers or sets of many types of values but at the same time they are immutable, like an immutable list, that is where tuples come in

tup_1 = ('hello',True,'Good Morning', 0.324, 1500, 'a', 4>6)

print(tup_1)

# tup_1[0] = 'world' #error because the tuple is immutable

#how to tell python this is a tuple --> use a comma under a bracket

new_tup = (1) #python thinks this is an int
print(type(new_tup))
new_tup = (1,) #now it knows this is a tuple
print(type(new_tup))

tuple_num = (1,23,45,45,61,78,999,9999,45,44.9999)

print(tuple_num.count(45)) # counts the total occurrences

print(tuple_num.index(23)) #gives first occurrence (index) of the given value
print(23 in tuple_num) # checks if a value is present in a tuple