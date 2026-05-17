# introduced in python 3.10, similar to the switch statement in c++ and java
# the syntax looks something like this

# consider a simple server example 

def http_status_codes(status_code:int):
    match status_code:
        case 200:
            print('OK')
        case 404:
            print('Not Found')
        case 500:
            print('Internal Server Error')
        case _:# this is similar to the default case / catch-all phrase in the switch statement
            print('Unknown Status')


http_status_codes(1000)




# Dictionary can be merged and updated in now as well


from typing import Dict

d : Dict[str,int] = {'a':12,'b':23}
d1 : Dict[str,int] = {'b':75,'c':3}

merged = d | d1

print(merged)

# we can also use multiple context managers in a single with statement using parantesized context managers, separated by commas

# Simply, we can open multiple files and write the code to modify them 

with(
    open('etc1.txt', 'r') as f1,
    open('etc2.txt', 'w') as f2
):
    content = f1.read()