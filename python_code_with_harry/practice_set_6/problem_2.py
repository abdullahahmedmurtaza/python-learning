marks_1 = int(input('Enter marks of the first subject : '))
marks_2 = int(input('Enter marks of the second subject : '))
marks_3 = int(input('Enter marks of the third subject : '))

percentage = ((marks_1+marks_2+marks_3)/300)*100

if(percentage>=40):
    print('You have passed')
else:
    print('You have failed')

