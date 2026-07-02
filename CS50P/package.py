# Python packages are third-party libraries, in the context of python, a package is a module implemented in a folder and not just a file

# The packages are available at pyPI --> pypi.org (python Package Index) which is searchable via the command-line AND the web

# packages like cowsay can be installed manually by doing everything ourselves

# Or we can use a package manager called 'pip' which is a program that comes with python and allows us to install everything smoothly.

# just run pip install cowsay in the terminal

import cowsay
import sys

if(len(sys.argv)) == 2:
    cowsay.cow('Hello, '+sys.argv[1])
    cowsay.trex('Hello '+sys.argv[1])

# Command line arguments are useful for devs and people who are BIG on automation because it is succinct, but it is not user friendly