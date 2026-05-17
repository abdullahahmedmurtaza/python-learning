# volatile --> data not saved
# non-volatile --> data is saved / it persists

f = open('test.txt') #built-in function, takes the file name and mode as params
data = f.read()
print(data)
f.close()

#writing in a file

st = 'Hello, world'

f = open('my_file.txt','w')
f.write(st)
f.close()

#readline and readlines

f = open('poem.txt')
line = f.readline()

print(type(line))
print(line)

f.close()


f = open('poem.txt')
line = f.readlines() #returns a list of lines

print(type(line))
print(line)
f.close()

#readlines() keeps reading until an empty string is found
#readline() + while loop --> same as readlines()

# append mode

f = open('test.txt','a')
f.write('Hey, this is appended')
f.close()

# rb for read binary , rt for read text (default)

# with statement is a better way to open file and make changes without needing to close it, follows the block syntax

with open('my_file.txt','a') as my_file:
    my_file.write('\n This is written using the with statement')
    
my_file = open('my_file.txt','r')
print(my_file.read())