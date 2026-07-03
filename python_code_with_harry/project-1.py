import random
computer_choice = random.choice([-1,0,1])
user_choice = input('Enter your choice (Snake, Water, Gun) : ')
play_dictionary_reverse = {
    1 : 'Snake',
    0 : 'Water',
    -1 : 'Gun',
}
play_dictionary = {
    'Snake' : 1,
    'Water' : 0,
    'Gun' : -1,
}
print(f'You chose {play_dictionary_reverse[play_dictionary[user_choice]]}, Computer chose {play_dictionary_reverse[computer_choice]}')

if(computer_choice == play_dictionary[user_choice]):
    print('Draw')
else:
    if(computer_choice == 1 and play_dictionary[user_choice] == 0):
        print('You Lose')
    elif(computer_choice == 0 and play_dictionary[user_choice]==1):
        print('You Won')
    elif(computer_choice == -1 and play_dictionary[user_choice]==0):
        print('You Won')
    elif(computer_choice == 0 and play_dictionary[user_choice]==-1):
        print('You Lose')
    elif(computer_choice == 1 and play_dictionary[user_choice]==-1):
        print('You Won')
    elif(computer_choice == -1 and play_dictionary[user_choice]==0):
        print('You Lose')
    else:
        print('Something went wrong....')
    
