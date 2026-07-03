words = ['Bad', 'Bura', 'Ganda', 'Wierd']

with open('content.txt', 'r') as f:
    content = f.read().lower()
    for word in words:
        content = content.replace(word.lower(), f'{len(word) * '*'}')
with open('content.txt','w') as f:
    f.write(content)



