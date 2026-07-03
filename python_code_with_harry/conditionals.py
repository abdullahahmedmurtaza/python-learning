#used to do something on the basis of a condition, simple if-elif-else blocks, there are no particular blocks using brackets but indentation can be used to signify the inside of a block.
a = int(input('Enter Your Age '))
if(a >= 18):
    print('You are able to vote')
elif(a<=0):
    print('Please Enter a valid age')
else:
    print('You are not able to vote')

print('END')

#multiple if statements are statements that are checked INDEPENDENTLY unlike elif blocks which are only checked like a ladder if the preceding if or elif is false.

#else needs if, elif needs if, if can be independent
