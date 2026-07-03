word = 'Donkey'

with open('content.txt','r') as f:
    content = f.read()
    content_new = content.replace(word.lower(),f'{len(word) * '*'}')

with open('content.txt','w') as f:
    f.write(content_new)


