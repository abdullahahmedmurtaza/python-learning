l = [1,2,3,4,5,6,15,25,55,60,68,32]
def div_by_5(n):
    if(n%5 == 0):
        return True
    return False

filtered = filter(div_by_5, l)

print(list(filtered))