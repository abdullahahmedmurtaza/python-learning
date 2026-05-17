def sum_till_n(n):
    if(n==0):
        return 0
    return n + sum_till_n(n-1)

print(sum_till_n(5))