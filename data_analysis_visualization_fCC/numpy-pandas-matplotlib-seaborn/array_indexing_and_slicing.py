# numpy uses the same indexing notation as python but it extends it a bit further by allowing multiple dimensions

# we can provide a comma separated list of indices or ranges to select a specific element or a subarray (also called a slice) from a numpy array

# This is used when we want to get data out of a numpy arra

import numpy as np
test_array = np.array([
    [
        [1,2,4,5,6,7],
        [23,44,3,2,1,8]
    ],
    [
        [34,55,6,1,21,55],
        [47,41,40,28,2,32]
    ],
    [   
        [19,44,31,32,66,75],
        [92,89,71,56,33,22]
    ],
])

print(test_array.shape)
print(test_array[2,0,4])

# we can provide ranges similar to lists (we will get a subarray so it does not alter the dimensions)

print(test_array[0:, 0, :2])

# to predict the output we can print the indices one by one and observe the result like test_array[0:] first then test_array[0:, 3] second etc. --> using only colon : preserves the entire dimension

# Practice

practice_array = np.array([0,1,2,3,4,5,10,11,12,13,14,15,20,21,22,23,24,25,30,31,32,33,34,35,40,41,42,43,44,45,50,51,52,53,54,55])

practice_array_reshaped = practice_array.reshape(6,6)

print(practice_array,'\n', practice_array.reshape(6,6))

# for 3,4

print(practice_array_reshaped[0,3:5])

# for 2,12,22,32,42,52

print(practice_array_reshaped[:,2:3])

#20, 22, 24, 40, 42, 44

print(practice_array_reshaped[2::2, ::2]) # Explanation : the slicing format is start, stop, step. start --> defaults to beginning, stop --> defaults to end, step --> defaults to 1, first part is for the row, second one is for the column

# 44, 45, 54, 55

print(practice_array_reshaped[4:,4:])
