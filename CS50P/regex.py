# Regular Expressions are used to define patterns in our code to check the received data / validation

# Let's validate an email address

email = input('Enter your email : ').strip()
if '@' or '.' in email:
    print('Valid')
else : print('Not Valid')

# Not a good approach gives valid for '@.', without username and the domain name.
username, domain = email.split('@')

# Short syntax --> if username --> gives back a True if the username is not a None or ''

if(username) and ('.' in domain):
    print('Valid')
else : print('Invalid')

# Academic top-evel domains end with .edu so let's check for that.

if username and domain.endswith('.edu'):
    print('Valid')
else : print('Invalid')
# This pattern is bypassed by malan@.edu --> no domain at all.

# The problems keep arising for just a simple check for whether something is an email address or not. 
# To improve this we have to use a python library called re --> for regular expressions

# Regular Expressions are patterns and re library allows us to define some patterns and validate them.

# refer to the official docs

# 1. re.search(pattern, string, flags=0) --> pattern is used to write the regex and the string is passed after that. Then we have flags to alter the behavior of this method

# Build an email pattern incrementally.

import re

if re.search('@',email):
    print('valid')
else : print('invalid')

# In regular expressions, symbols are used to define patterns.
# No need to learn all the symbols. Few symbols are used 90% of the time
# . --> any character except a new line
# * --> 0 or more repetitions
# + --> 1 or more repetitions (at least 1)
# ? --> 0 or 1 repitition
# {m} --> m repetitions
# {m,n} --> m-n repetitions (m through n)

# .* means any char any repetitions
# the equivalent of + is ..* --> any character, then 0 or more of any character 

if re.search(r'.*@.*',email):
    print('Valid')
else : print('Invalid')

# How does the computer check for the pattern that is passed? It uses a machine (Non-deterministic finite automata to solve this problem).
# Useful but not mandatory for this right now.

# if re.search(r'.+@.+.edu',email): 
# To solve the domain problem, we need the .edu but . has a special meaning in regex. we have to escape it using backslash
if re.search(r'.+@.+\.edu', email):
    print('Valid')
else : print('Invalid')

# Always use r with regular expressions to tell python about a raw string.

# Google Forms also allows response validation using regular expressions

# The current regular expression allows users to type in a full english sentence like "My name is malan@harvard.edu" and it will still be treated as valid but we do NOT want that

# To handle this (to get only the email) we need 2 more symbols
# ^ --> matches the start of the string
# $ --> matches end of the string just before the newline

# Refined expression becomes

if re.search(r'^.+@.+\.edu$', email):
    print('Valid')
else : print('Invalid')

# This expression allows multiple @@@ to exist. we have to define a pattern that allows only one.

# For this we have two new symbols
# [] --> for a set of characters we want / match
# [^] --> for a set of characters we do not want / cannot match

# Regex --> r'^[^@]+@[^@]+\.edu$'

if re.search(r'^[^@]+@[^@]+\.edu$', email):
    print('Valid')
else : print('Invalid')

# This validation fails at .edu@something.edu
# There are standards for the username part of an email and an email in general.

# username can have alphanumeric characters [a-zA-Z0-9_]
# The alphanumeric pattern is common so it has a shortcut which is \w

# Regex --> '^\w+@\w+\.edu$

# There are other patterns as well
# \d --> decimal
# \D --> not a decimal
# \s --> whitespace
# \S --> not a whitespace
# \w --> alphanumeric + underscore
# \W --> not a word 

# We can also group and check the domains .com/.gov etc. () --> group | --> or 
# (a|b)
# (?:a|b) --> not a or b 

# What if we type everything in uppercase the .edu will not be matched then.

# To fix this we use flags re.IGNORECASE, re.MULTILINE, re.DOTALL.
# Names are self-explanatory DOTALL makes . recognize all chars AND the new line as well.

# What if we require multiple subdomains as well e.g malan@cs50.harvard.edu

# There are two dots and if we add another \w\. then the original top-level domain breaks. Better approach : Group them in parentheses and use ? which means 0 or more (optional).
# (\w+\.)?

# The official Regex that the browsers use nowadays (catches most mistakes but not all) --> /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/ 

# Better to use libraries for common validations :)

# There is another method called re.match(pattern, string, flags=0) --> same as search but doesn't require the ^ at the start.

# Similarly fullmatch --> checks the entire string.
