
# Here we are adding multiple arguments to the argv vector

# Since the [0] is the name of the program we are taking out a slice from the list --> [start : end] inclusive, omitting values means going all the way. whereas using -ve indices starts from the end.

# Visualize -ve indices by using length - 1 in the mind

import sys
for arg in sys.argv[1:]:
    print(f'Hi! my name is {arg}')