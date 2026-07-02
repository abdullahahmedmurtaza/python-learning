import numpy as np

# We have seen how to create numpy arrays like np.array(), and np.genfromtxt

# Now we look at how to create some special types of arrays

# All zeros

zero_arr = np.zeros((3,2)) # takes tuple for dimension
print(np.int64(zero_arr))

# All ones

one_arr = np.ones((3,4))
print(np.int64(one_arr))

# Identity matrix

identity = np.eye(3)
print(np.int64(identity))

# rand --> selects a value b/w 0 and 1, randn --> selects a value from a gaussian distribution (-2,2) use randn more than rand

random_array = np.int64(np.random.randn(3,3))
print(random_array)

# identity and rand / randn functions do not need a tuple

# Fixed values

full_array = np.full((3,4),45)
print(full_array)

# creating an array with start stop step

skipped_array = np.arange(12,55,2)
print(skipped_array)

# Equally spaced numbers in a range

eq_space_array = np.linspace(3,27,9)
print(eq_space_array)

# argument means start, stop, how many numbers?

# For further reference use numpy docs (especially the reference section)