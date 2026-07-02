# Suppose we have to remove the name of a user from the twiter url. 
url = input('Enter the URL : ')
username = url.replace('https://twitter.com/','')
print(username)
# Kind of works as expected but we need a better approach to handle various protocols, the user might not type https --> they can use www/directly twitter.com. and the URL might be longer with http parameters as well
# Overall this code is fragile.

# The code also accepts the entire english string "My name is abdullahahmedmurtaza" but we only want the username, nothing more.

# we can use the removeprefix method but it still won't work.

# For this we have to use a re.sub(pattern, repl, string, count=0, flags=0)
# takes : pattern --> what to check, repl --> what to replace it with, string --> what to check against. It is essentially find and replace
import re
username = re.sub(r'https://twitter.com/', '', url)
print(username)

# The pattern allows all the characters after twitter because of the .
# The protocol can be https or http

username = re.sub(r'^https?://twitter\.com/', '', url)
print(username)

# We now want to handle the www. which may or may not exist in our browser.

username = re.sub(r'(https?://)?(www\.)?twitter\.com/','',url)
print(username)

# Never try to write the entire regex at once always use increments and check whether it works or not.

# We specifically want the twitter username but this one allows google urls as well so let's fix it using the search approach with if and a walrus operator


if matches := re.search(r'^(https?://)?(?:www\.)?(twitter\.com)/(.+)$',url,re.IGNORECASE):
    print(f'Username : {matches.group(3)}')
else :
    print('Invalid URL')

# () matches and captures the matched items to access them using .group()
# (?:) groups but does not capture the matched items

# twitter in the username supports only alphanumeric chars and underscore

if matches := re.search(r'^(https?://)?(?:www\.)?(twitter\.com)/([a-z0-9_]+)$',url,re.IGNORECASE):
    print(f'Username : {matches.group(3)}')
else : print('Invalid URL')

# There are also other methods like re.split(pattern, string, maxsplit=0, flags=0) and re.findall(pattern,string,flags=0) which allows us to find multiple copies of the same pattern in different places in a string