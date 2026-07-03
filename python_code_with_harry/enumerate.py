l = [3,315,21,44,23]


# This is a very long process so, it can be simplified using enumerate

# index = 0
# for i in l :
#     print(f'The item at index {index} is {i}')
#     index += 1


for index, item in enumerate(l):
    print(f'The item at index {index} is {item}')

#Used to print item and index at the same time without keeping track of the index manually

