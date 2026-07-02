import csv




# Storing data in variables is good but it immediately goes back as soon as we exit the program. This is not super useful in todays world, we want the data to persist.

# Suppose we have a list of student names
names = []

for _ in range(3):
    names.append(input('Enter your name : '))
for name in sorted(names):
    print(f'Hello, {name}')

# The names are gone as soon as the program terminates
# open keyword opens a file or creates if it is not already created (equivalent to double-clicking on an a file), it needs the name of the file and how to open it.

open('file_by_python.txt', 'w') #Open returns a file handle so store it in a variable

names = []

with open('file_by_python.txt', 'a') as f:
    for _ in range(5):
        f.write(f'{input('Enter the name : ')}\n')

with open('file_by_python.txt') as f:
    for line in sorted(f):
        names.append(line.rstrip())

for name in names:
    print(name)

# sorted function takes a list and reverse which is False by default but it can be set to True.

# to manipulate the data use a lines variable to store lines as a list.

# A better way to store data is csv which is comma separated values.

# CSV stores multiple RELATED PIECES OF INFORMATION
# In the program we take the entire line and separate things based on a comma

print('------------------------------------------------')
with open('names.csv') as f:
    for line in f:
        # print(line.rstrip().split(',')[0])
        # Much better approach would be to unpack things and store them in variables
        name, house = line.rstrip().split(',')
        print(f'{name} is in {house}')

students = []
with open('names.csv') as f:
      for name in f:
          name, house = name.rstrip().split(',')
          students.append(f'{name} is in {house}')
for student in sorted(students):
    print(student)

# Sorting is done by entire english sentences, what if we want to sort specifically by name or by house?

# For this we use a dictionary
# Step 1 --> Empty dictionary
# Step 2 --> assign the extracted values to a key e.g dictionary['key_name'] = extracted_value
# Step 1 --> append the dictionary to the list (list.append(dictionary))



students_new = []
with open('names.csv') as f:
      for name in f:
          name, house = name.rstrip().split(',')
          student = {'name' : name, 'house' : house}
          # We can also assign the keys and values at the time of creating a dictionary
        #   student['name'] = name
        #   student['house'] = house
          students_new.append(student)
        # Now we cannot simply sort the list because each element in the list contains a dictionary, rather, we want to sort by a particular value in the dictionary.

        # the sorted function takes a named parameter known as key to specify the key by which to sort. We can use a simple lambda function that returns the value of the key from the dictionary one by one. When using a standard function always keep in mind to pass it by name without parentheses

        # We are passing a function as an argument to another function.
for student in sorted(students_new, key=lambda student : student['name']):
    print(f'{student['name']} is in {student['house']}')

# What if the value of something in the csv contains a comma gramatically? what then? We get a ValueError.

# We can change our separatr or change our code to only select those values which contain a comma but are inside quotes etc. but this can get really messy really fast.

# This is why we use the csv library in python (can be found in docs)

# The csv module comes with a built-in function called reader() which reads the file passed as an argument.

with open('students.csv') as f:
    reader = csv.reader(f)
    for name, home in reader:
        print(name, home)

# Instead of a reader use a DictReader with a header in the csv file as well it treats the columns as a dictionary of columns, much better for using different softwares to manage the csv. (apple numbers, excel, google sheets etc.)

with open('students.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f'{row['name']}, {row['home']}')

name = input('Enter the name...')
home = input('Enter the home...')

#  We can also write a csv using a writer method
with open('students.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow({'name':name, 'home':name})

# In addition to text we can also work with binary files which are 0s and 1s arranged to represent audio, video, graphics etc.

# For this there is also a built-in library called PIL (pillow) to work with images and animate them in gifs

from PIL import Image
import sys

images = []
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    'costumes.gif',
    save_all = True,
    append_images=[images[1]],
    duration=200,
    loop=0
)

