# flags are used to define some particular behavior of a program.
# single dash is used with a single letter, double dash is used for a word

import sys
if(len(sys.argv)==1):
    print ('time')
elif(len(sys.argv)==3 and sys.argv[1] == '-n'):
    n :int = int(sys.argv[2])
    print('time\n'*3,end='')
else:
    print('usage = handling_command_line_args.py')

# What if we want to use -a, -b etc. for multiple behaviors?
# We have to use a library called argparse.

import argparse
parser = argparse.ArgumentParser(description='Print name n times')
parser.add_argument('-n',default=1,help='Number of times to print the name',type=int)
args = parser.parse_args()
for _ in range(args.n):
    print('abdullah')

# the code works as inteded but there are two points :
# 1. the code does not work when we don't pass in an arg (it should print 1 by default)
# 2. the code does not provide significant help when we run it with -h or --help.

# the ArgumentParser takes a description as a string to describe the function.

# the add_argument function also takes a help parameter --> describe what the flag does

# the default arg is passed in add_argument to give a default value of n.
# in add_argument, we can also specify the type of the argument. e.g type = int, then we do not have to convert it in the loop.

# [] --> square brackets in documentation mean that the values are optional.


# This is why we use libraries, to make our work easier, and to ocus on the actual code.