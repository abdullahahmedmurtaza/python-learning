from random import randint

random_number = randint(1,100)
a = 0
guesses = 1
while(a!=random_number):
    a = int(input('Enter a number between 1-100 : '))
    if(random_number>a):
        print('Guess greater please')
        guesses +=1
    elif(random_number<a):
        print('Guess Lower Please')
        guesses +=1

print(f'You found the correct number {random_number} in {guesses} guesses.')
