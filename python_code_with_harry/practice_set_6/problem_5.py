l1 = ['Abdullah','Ali','Khan','Raees','Rizwan','Muhammad']
name = input('Enter the name to check : ')

if(l1.__contains__(name)): # if (name in l1)
    print('Name found')
else:
    print('Name not found')