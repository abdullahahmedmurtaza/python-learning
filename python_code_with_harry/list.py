#lists are containers to store multiple values of various data types, because strings are immutable that is why we use lists which are mutable/original list is changed.

#list slicing is the same as string slicing

friends = ['abdullah','pritam','muzammil']

friends [0] = 'avinash'

print(friends)

# name = 'abdullah'
# newName = name[0] = 'g'
# print(newName)

#error because of immutability

print(friends[1:2])

#list methods
friends.append('Harry')
print(friends)

# if a method mutates/ modifies in place it does not return anything, to avoid confusion like l1 = l1.sort()

l1 = [1,2,3,544,0.99999,233232436,89896,4312,354,9646743]
l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.insert(3,'laaatrine') #adds at a particular index
print(l1)

print(l1.pop(3)) #pops from given index, returns a value
print(l1)

l1.remove(544) #removes a value from a list, takes the value as a parameter