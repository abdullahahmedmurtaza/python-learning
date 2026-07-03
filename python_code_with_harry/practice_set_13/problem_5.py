from functools import reduce

# IMPORTANT : ALWAYS THINK OF CONVERGING THE PROBLEM WHEN DEFINING A FUNCTION FOR THE REDUCE FUNCTION, KEEP TWO-TWO COMBINATIONS IN MIND

l = [2,7,8,4,5,6,44,3,333]

def greater(a,b):
    if(a>b):
        return a
    return b

res = reduce(greater, l)
print(res)