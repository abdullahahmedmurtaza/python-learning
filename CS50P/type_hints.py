# Python is dynamically typed --> we do not have to specify the type of a variable
# We can however provide something called type hints which allow us to check the type by using a package/program called mypy --> pip install mypy --> mypy.readthedocs.io, but the language itself does not enforce it.

# type hints --> : str or : int etc.

def meow(n :int) -> str:
        return 'meow\n' * n
n :int = int(input('How many times do you want the cat to meow? '))
print(meow(n), end = '')

# All the functions by default/implicitly return None. so we can annotate that as well by -> None

# It is better to return a value rather than a side-effect like printing

# Docstrings are special types of strings used in documentation of methods to tell people about a method

# They follow a certain convention as well

'''

        prints something n times
        :params : n, user_input
        :type n :int
        :type user_input :str
        :raise TypeError : If n is not an int or user input is not a string
        :return: A string of user input, n times on a new line
        :rtype: str
'''