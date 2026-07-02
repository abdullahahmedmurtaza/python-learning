ans = input('What is the Answer to The Great Question of Life, the Universe and Everything? ')
if ans.strip() == '42' or ans.lower().strip() == 'forty-two' or ans.lower().strip() == 'forty two':
    print('Yes')
else:
    print('No')