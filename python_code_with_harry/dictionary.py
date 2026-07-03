#dictionary in python is a collection of key value pairs, nothing more, a list of key-value pairs.

marks = {
    'Abdullah' : 12,
    'Ali' : 34,
    'Khan' : 22,
    'Rizwan' : 34
}

#elements can be accessed using their keys,can be implemented using a list of lists but dicts have fast lookup O(1)

#unordered, mutable, no duplicate keys, indexed, not necessary that key must be a string. 0 : 'Abdullah' is valid

print(marks, type(marks))
print(marks['Khan'])

#methods for dictionary

print(marks.items()) #gives a list of key value pairs in the form of a list of tuples
print(marks.keys()) #gives a list of keys in the form of a list
print(marks.values()) # gives a list of values in the form of a list

#these are view object they look like list or tuples but aren't one bcz of memory management and real-time change reflection
marks.update({"Harry" : 100, "Rizwan" : 32})
print(marks)

#important difference in syntax print(marks.get('Harry')) --> returns None if there is no key, but print(marks['Harry']) --> gives error if there is no key

marks.pop('Harry', 'default') # pops acc to the given key, if the key is not found gives the default if the default is not found gives KeyError

marks.popitem() #removes and returns the last key item (LIFO) method

marks.clear()#clears the entire dictionary