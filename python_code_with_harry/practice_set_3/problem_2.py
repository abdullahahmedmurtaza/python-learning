name = 'Abdullah'
date = '24/03/2026'

letter = f'''
    Dear {name},
    You are selected!....
    {date}

'''


print(letter)

#alternate approach

letter2 = '''
    Dear <Name>,
    You are selected!
    <Date>
'''

print(letter2.replace('<Name>','Abdullah').replace('<Date>','24/03/2026'))
#because strings are immutable so python returns a new string and that string can be treated as a new string on which the method is applied by chaining