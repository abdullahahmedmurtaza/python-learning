with open('old.txt','r') as f:
    content = f.read()
with open('renamed_by_python.txt','w') as f:
    f.write(content)

#Better approach is to use the os module or the shutils module. because in the above code the file is not deleted