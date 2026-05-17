username = input('Enter your username : ')

if(len(username)<10):
    print('Username is too short')
else:
    print(f'Accepted username : {username}')