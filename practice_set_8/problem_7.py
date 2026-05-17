list = ['Abdullah','Huzaifa','Hamza','Ammar','Fahad','Mubashir','Rohan','an', 'Hannan']

def rem_strip(l,word):
    n = []
    for i in list:
        if(not(i == word)):
            n.append(i.strip(word))
    return n

print(rem_strip(list, 'an'))



