# working with data : Data in data analysis with python basically means numerical figures such as stock prices, sales figures, database tables, sports scores etc.

# for this we use a library called numpy (numerical python) to perform numerical computation

# Q: Why do we need numpy because python already has a lot of built in operations?

# This question is explained with the help of an example
# Suppose we need to find out the yield of apples in multiple regions by formulating a relationship between the annual yield of apples (tons per hectare) and 
# the avg temperature, 
# rainfall, 
# and avg humidity
# we can represent this using a linear equation
# yield_of_apples = w1 * temperature + w2 * rainfall + w3 * humidity

# w1 , w2 , w3 are the weights extracted from some historical data
# We are representing the relationship as a linear weighted sum of the factors, which is an approximation as the actual relationship may not be linear, but this model works well in practice.

# consider we have the table for 5 regions and using simple python we store them in variables we will get 15 variables. (not suitable for larger datasets)

# by using this we can substitute these values in the equation given above, and we will get the yield for a region. IT IS POSSIBLE

# A more simpler , practical , and easy approach is to use vectors for this, where the weights are one vector, the factors are another and we take a dot product between them

# CONSIDER THIS CODE EXAMPLE BELOW

weights = [.3,.2,.4] 

karachi = [73,55,67] 
lahore = [89,12,43] 
bahawalpur = [77,11,76] 
multan = [84,13,32] 
hyderabad = [91,47,15]

def yield_calculator(w:list,reg:list):
    res = 0
    for x,y in zip(w,reg):

        # The zip method takes two elements from two lists and merges them together in the form of a tuple, VERY USEFUL
          
        res += x*y
    return res

print(str(yield_calculator(weights,karachi))+' Tons per Hectare')


#Numpy library allows us to do the numerical computation with ease, for example it has a dot product method built-in which can easliy perform the dot product of two vectors but only if they are numpy arrays

import numpy as np

# to create a numpy array use np.array()

kanto = np.array([73,67,43])
print(kanto, type(kanto))

weights = np.array([12,22,32])
print(weights , type(weights))

# Numpy arrays behave just like lists, and they also support index notation

print(kanto[0])
print(weights[2])
