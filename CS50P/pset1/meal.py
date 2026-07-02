def main():
    current_time = input('What is the time? ')
    tell_meal(convert(current_time))

def convert(time):
    time = time.strip()
    hours,minutes = time.split(':')
    converted_time = int(hours) + int(minutes)/60
    # print(converted_time)
    return converted_time

def tell_meal(t):
    if 7 <= t <= 8:
        print('breakfast time')
    elif 12 <= t <= 13:
        print('lunch time')
    elif 18 <= t <= 19:
        print('dinner time')
    else:
        print('Invalid Time....')


if(__name__ == '__main__'):
    main()