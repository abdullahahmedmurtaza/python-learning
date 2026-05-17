input_num = int(input('Enter the number : '))

# i = input_num
# fact = 1
# while(i>0):
#     fact = fact * i
#     i-=1
# print(fact)









# range goes forward by default so the best way is to multiply forwards or if we want to go backwards, we have to do -1 step



# if(input_num==0 or input_num==1):
#     print('1')
# else:
#     fact = 1
#     for i in range(input_num,0):
#         fact = fact * i
#     else:
#         print(fact)


if(input_num==0 or input_num==1):
    print('1')
else:
    fact = 1
    for i in range(input_num,0,-1):
        fact = fact * i
    else:
        print(fact)