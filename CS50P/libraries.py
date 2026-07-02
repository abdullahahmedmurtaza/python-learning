# Libraries or modules are files of code that someone else has written or even you have written and you want to use it in your own projects again again

# It is a means of sharing code with others and across or your own projects as well

# module has one or more functions to encourage reusability

# python comes with a 'random' library which is automatically installed. sometimes functions are tucked away in libraries (file called random.py) so we have to load them in the computer's memory

# import keyword is used to load a library

import random as rd
# functions are used by using dot e.g rd.choice(seq) --> seq means sequence like a list or something list-like (more in docs)

# Simulating a coin-toss

coin = rd.choice(['heads','tails'])
print(coin)

# It might look rigged short-term but the probability is 50/50

# We can use the keyword 'from' to load particular function names into our file's namespace 

# from random import choice
# Now, I can write choice instead of random.choice

#  import random enables scoping of methods to avoid naming collisions

# random.randint(a,b) --> prints an int between a and b inclusive

print(rd.randint(1,10))

# random.shuffle(x) --> shuffles, randomizes a list

cards = [
    "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
    "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
    "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
    "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC"
]
print(rd.shuffle(cards))  
# We get None because it actually shuffles the entire list itself, doesn't return anything

for card in cards:
    print(card)

# Probability can be askewed using sophisticated functions from this library as well as others.