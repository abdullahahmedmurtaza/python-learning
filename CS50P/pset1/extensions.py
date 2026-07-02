filename = input('Enter the file name : ').lower()
extension = filename.split('.')[1]
# print(extension)
match extension:
    case 'gif':
        print(f'image/{extension}')
    case 'png':
        print(f'image/{extension}')
    case 'jpeg' | 'jpg':
        print(f'image/jpeg')
    case 'pdf':
        print(f'application/{extension}')
    case 'txt':
        print('text/plain')
    case 'zip':
        print(f'application/{extension}')