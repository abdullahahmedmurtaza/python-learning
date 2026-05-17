#loops are used to do something repeatedly

for i in range(1,6): #the range is similar to the indexing in the list except for cround brackets and a comma instead of a semicolon, the last one is excluded. 
# range function provides a sequence (always include full length to go len-1), range can be applied on iterables like strings, lists, tuples, skipping is also allowed by the step_size
    print(i)


#simple while loop
i=1
while(i<11):
    print (i)
    i+=1

#loops in iterables

l = ['chacha', 'chachahhh', 'chahchahhhh', 'waaste', 'wasteganahoiyeeeee', 'chachahhhhuhhhh']


for i in l: #this syntax assumes the starting as 0
    print(l[i])

tup = ('1',True,'dfhklhfkal',32.6,3,'fkg')

for i in tup:
    print(tup[i])

my_str = 'Abdullah'

for i in my_str:
    print(i)
else:
    print('This is the else block in for') #runs when the for loop is about to be exited / when it is exhausted

#break --> breaks (exits the loop completely), continue --> skips the current iteration (continues for the next iteration), pass --> if a for loop is written and nothing is specified, python thinks the loop is incomplete so to give a null value we use pass / used to work on other things and come back to the for loop 