def check_for_twinkle(file_path):
    f = open(file_path, 'r')
    data = f.read()
    if('twinkle' in data.lower()):
        return True
    return False

print(check_for_twinkle('poems.txt'))