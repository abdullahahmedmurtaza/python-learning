#strings are immutable in python, reverse counting means reverse order -1 -2 -3 etc, slicing can also be done in python strings but the last index is not included.


#negative indices are solved by converting them into their corresponding positive indices.

#by default if the first is blank --> 0 index, if the last is blank --> length

test_str = 'This is my test string'

test_str_short = test_str[-1]
print(test_str_short)

test_str_slice = test_str[0:3] 
print(test_str_slice)

test_str_neg = test_str[-4:-1] 

print(test_str_neg)

#slicing can also be done with skip values, first resolve the slice after that jump the given places, for jumping just add the jump to the current index

num_test_str = '0123456789'
print(num_test_str[1:7:3])

print(num_test_str[:])


#string methods
test_str_2 = 'Abdullah'
print(len(test_str_2))
print(test_str_2.endswith('lah'))
print(test_str_2.startswith('Abd'))
print(test_str_2.capitalize())
print(test_str_2.find('lah')) #finds the index in the parent string and gives -1 if the matching string is not found
print(test_str_2.replace('lah','b'))


