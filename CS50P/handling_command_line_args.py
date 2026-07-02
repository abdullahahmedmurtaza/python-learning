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
parser = argparse.ArgumentParser(description='Print anything n times')
parser.add_argument('-n', help='number of times to meow')
args = parser.parse_args()
for _ in range(int(args.n)):
    print('abdullah')
