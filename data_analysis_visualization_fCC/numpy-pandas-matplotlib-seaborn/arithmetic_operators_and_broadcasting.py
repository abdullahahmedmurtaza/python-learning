import numpy as np
# Numpy supports arithmetic operators like + - * etc. 

myarr = np.array([
    [12,33,21,44],
    [22,435,64,421]
])

print(myarr)

myarr2 = np.array([
    [11,43,87,99],
    [22,128,21,32],
])

print(myarr+myarr2)

print(myarr+3)

print(myarr - myarr2)
print(myarr / 2)
print(myarr * myarr2)
print(myarr2 % 2)

# Numpy arrays also support broadcasting. It is a concept which allows arithmetic operations between arrays having different dimensions but compatible shapes. Consider the example given below

print(myarr.shape)
print(myarr2.shape)

# If the shapes are like (2,4) and (4,) we can perform broadcasting on it. where the array with (4,) gets replicated 2 times to match (2,4)

test_arr_1 = np.array([
    [1,2,3,4],
    [5,6,7,8],
])

test_arr_2 = np.array([1,5,6,7])

print(test_arr_1.shape, test_arr_2.shape)

# Replicating in test_arr_2

print(test_arr_1 + test_arr_2)

# Broadcasting is useful because numpy does not actually create copies of the smaller dimension array

# broadcasting can only be applied if one array can be replicated to exactly match the shape of the other array

# Simply, only the rows are replicated, not the columns

# Along with arithmetic operations, numpy also supports comparison operators

print(test_arr_1 == test_arr_2) # returns a boolean array (element wise comparison)

# HOW TO CHECK THE NUMBER OF EQUAL ELEMENTS IN AN ARRAY

print((test_arr_1 == test_arr_2).sum()) # the .sum() will treat true as 1 and false as 0 (truthy and falsy values)