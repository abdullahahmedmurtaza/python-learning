input_text = input('Enter the message : ')
if input_text.__contains__(':)') or input_text.__contains__(':('):
    new_text = input_text.replace(':)','🙂')
    print(f'{new_text.replace(':(','🙁')}')  
else :
    print('Invalid emoticon ( use ":)" or ":(" )')