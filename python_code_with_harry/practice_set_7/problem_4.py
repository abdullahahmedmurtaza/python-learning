input_num = int(input('Enter any number : '))
for i in range(2,input_num):
    if(input_num%i == 0):
        print('not prime')
        break
else:
    print('prime')
       

