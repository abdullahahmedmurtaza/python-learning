import os 

# Specify the directory you want to list 
directory_path = "/Ahmed"

# List all the file and directiories in a specified path
contents = os.listdir(directory_path)

# print all the items one by one
for item in contents :
    print(item)