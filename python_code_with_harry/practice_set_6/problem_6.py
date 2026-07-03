marks = int(input('Enter your marks : '))

if(marks<=100 and marks>=90):
    grade = 'Ex'
    print('Your grade is : ', grade)
elif(marks<90 and marks>=80):
    grade = 'A'
    print('Your grade is : ', grade)
elif(marks<80 and marks>=70):
    grade = 'B'
    print('Your grade is : ', grade)
elif(marks<70 and marks>=60):
    grade = 'C'
    print('Your grade is : ', grade)
elif(marks<60 and marks>=50):
    grade = 'D'
    print('Your grade is : ', grade)
else:
    grade = 'F'
    print('Your grade is : ', grade)