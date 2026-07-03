# The dot product can be calulated for any two numpy arrays (vectors) by using np.dot(arr1,arr2)

import numpy as np 

kanto = np.array([12,22,33])
weights = np.array([13,42,83])

print(np.dot(kanto,weights))

# numpy arrays support even lower level operations so we can achieve the same result as well by performing multiplication and then addition. 

# if we use * operator on numpy arrays it does an element-wise multiplication and returns the vector

print(kanto * weights)

# similarly + does element wise addition

print(kanto + weights)

# Important distinction between .sum and the + operator
# .sum() return the sum of all the elements in a vector while the + sums two vectors element-wise

print(kanto.sum())

# Alternative way of dot product

print((kanto * weights).sum())

# This provides us with a very nice way to write an expression without having to write a function or loops

# numpy is better in performance as well because internally it is implemented using c++ and the python interpreter is minimally involved

# np.dot is 100 times faster than using a for loop


# MULTIDIMENSIONAL NUMPY ARRAYS 

# We can represent the data of all the regions in a single multidimensional array as well

climate_data = np.array([
    [44,55,21],
    [33,51,67],
    [44,51,25],
    [21,33,44],
    [21,33,45]
 ])

# This is just a matrix with 5 rows and 3 columns

# Similarly we also have 3D arrays, which have the three dimensions. Numpy arrays can have any number if dimensions and different lengths across each dimensions. we can inspect the length along each dimension by using the .shape property

print(climate_data.shape)

# it returns (5,3) as there are 5 elements in th outermost array, and there are 3 elements in each of those arrays. 
# Rule of thumb : Start counting from the outside and move in step by step

print(weights.shape) 

# returns (3,) because there are only three elements (1D array)

three_d_array = np.array([
    [[3,4]],
    [[4,4]],
    [[5,5]],
    [[6,6]],
    [[7,1]]
])

print(three_d_array.shape)

# Prints (5,1,2) as the shape --> moving inwards from the outermost list.

# Data types of all the elements in an array must be same. check using the dtype property

print(weights.dtype)

# if an array contains even 1 float all the other elements are converted into floats as well.

float_arr = np.array([12,22,33.5])
print(float_arr.dtype)

print(float_arr) # all are converted to floats

# Python has many primitive data types which allow a wide range of values but numpy has int64 and float64 so it limits the range to 64 bits.

# Important terms --> Axis : Dimensions, Length along each axis : how many elements each dimension contains

# Now, we can find the yield of apples in all the regions by doing matrix multiplication 

# Dot product --> multiplies the vectors and returns a single scalar value 

# Cross product (matrix multiplication) --> multiplies the vectors and returns another vector

# For matrix multiplication the .matmul() method or @ is used

print(np.matmul(climate_data,weights))
print(climate_data @ weights)

# In this way we get the yield for all the 5 regions






