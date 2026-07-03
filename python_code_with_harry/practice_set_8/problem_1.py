def greatest_of_three(a,b,c):
    if(a>b and a>c):
        print(f'The greatest is {a}')
    elif(b>a and b>c):
        print(f'The greatest is {b}')
    elif(c>a and c>b):
        print(f'The greatest is {c}')
    else:
        print('Something went wrong...')

greatest_of_three(12,339,4500)