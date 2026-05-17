#python loops over a string char by char using the in keyword

# Exactly — the character-by-character behavior comes from the for loop, not from the in keyword itself.

# But here’s the subtle (and important) truth:

# in behaves differently depending on how it’s used.

# 1. for ... in ... → iteration
# for x in "python":
#     print(x)

# Here, in means:

# “Take elements one by one from this iterable”

# Since a string is an iterable of characters, you get:

# p
# y
# t
# h
# o
# n

# So yes — this is where the char-by-char behavior comes from.

# 2. "something" in string → membership test
# "python" in "I love python"

# Here, in means:

# “Does this substring exist inside the string?”

# No looping at your level, no character-by-character exposure — just a True/False check.

# Same keyword, different roles

# Python reuses in for two related but different concepts:

# Usage	Meaning
# for x in y	iterate over elements of y
# x in y	check if x is contained in y
# A helpful way to think about it
# for x in y → “give me each piece of y”
# x in y → “is x inside y?”
# One last detail (useful insight)

# Even though:

# "python" in cont

# doesn’t look like a loop, Python is still checking internally — but:

# it’s done in optimized C code
# it searches for a sequence, not individual characters you interact with
# Bottom line
# ✅ Your intuition is now correct
# ❌ The issue was never the in keyword itself
# ✅ It was how you used it with a for loop

# If you keep this distinction clear, you’ll avoid a whole class of bugs going forward.

keyword = 'Python'

def read_file():
    with open('log.txt','r') as f:
        content = f.read().lower()
    return content

def check_for_keyword():
    cont = read_file()
    if(cont.__contains__(keyword.lower())):
        return True

def count_occurences():
    cont = read_file()
    count = cont.count(keyword.lower())
    return count

print(check_for_keyword())
print(count_occurences())



#alternative solution

with open('log.txt','r') as f:
    content = f.read()
if('python' in content):
    print('Python is present')
else:
    print('Python is not present')