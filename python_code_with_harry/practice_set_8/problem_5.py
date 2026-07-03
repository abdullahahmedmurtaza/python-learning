def print_star_pattern(n):
    if(n==0):
        return
    print(n*'*')
    print_star_pattern(n-1)

print_star_pattern(5)