def my_func():
    print('Hi! this is my func')

my_func()

#__name__ tells which file is running the code
# from the imported file --> name of the file
# from the actual file __main__

print(__name__)


# it is used to block some of the code from being executed if it is imported

if(__name__ == '__main__'):
    print('Running directly from the file in which the code is written')