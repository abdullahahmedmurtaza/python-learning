# CSV means comma separated values. 
# The first line describes the data points and below that all the lines represent one data point. e.g the climatic conditions for one region
# It basically stores the tabular data (numbers + text) in comma separated form and plaintext form

# we are going to import a file using the urllib library which provides a lot of tools form working with urls, making requests etc. (.request is a submodel of urllib)

from urllib.request import urlretrieve
import numpy as np

# ----------------------------------------------------------------

# urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/08/climate.csv', 'climate.txt')

# Doesn't work for some reason

# -----------------------------------------------------------------

# Now the first thing to do is to load it as a numpy array. Because it contains all numbers

# for this we will use the genfromtxt(file_name, separator(delimiter) , skip_header) method from the numpy library

climate_data = np.genfromtxt('climate.csv', delimiter=',', skip_header=1)

# the delimiter can be a comma or a tab character

print(climate_data, '\n',climate_data.shape)

# Task -- Given the weights calculate the yield for all the regions

weights = np.array([0.3, 0.2, 0.5])
yields = climate_data @ weights

print(yields)

print(yields.shape)

# Now we have to add the results as a column back to the file

# The np.concatenate() method is used to join two arrays, It needs two arguments. 

# 1. A tuple containing the arrays, and the direction (axis) along which you want to join them (outermost axis = 0, one step in = 1)

climate_results = np.concatenate((climate_data, yields.reshape(10000,1)),axis=1)
print(climate_results)

# We have to use reshape(1000,1) to match / change the dimensions 
# This is also called changing the shape


# climate_results = np.concatenate((climate_data, yields),axis=1)

# when axis = 0 it joins below, when the axis = 1 it joins above

# ValueError: all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s) 

# The doumentation for the numpy functions can be accessed using .help() function

# Now we have to write the data back to the file, there is a function for this also in numpy

np.savetxt('climate_results.txt' , climate_results, fmt = '%.2f', header='temperature, rainfall, humdity, yield_apples', comments='')

# Numpy provides many functions for performing operations on arrays no need to memorize all of them, just use google or AI to search what you need in a concise manner

# The list of all functions is present in numpy docs



