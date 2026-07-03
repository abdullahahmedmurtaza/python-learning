# In this file we will be looking at generators
# Suppose we build a program that prints sheep

# def main():
#     sheep(int(input('How many sheep? ')))

# def sheep(n):
#     for i in range(n):
#         print('🐑'*i)
#         print()

# This works fine but breaks when we try to print 1 million sheep, we can also use a list to store all of the flock and then return the entire list

# def sheep_flock(n):
#     flock = ['🐑' * i for i in range(n)]
#     for sheep in flock:
#         print(sheep)
        
# sheep_flock(4)

# prints n-1 as it starts from 0
# However this also breaks the Computers memory / resources at 1 million.

# This is where generators come in --> we use the yield keyword to return the values one at a time dynamically while keeping the state of the function maintained, basically it allows us to return values in a loop

# While using yield it is important to print the values using a loop on the function itself like  -->   for s in sheep_yield(3):
                                # print(s)

# yield always return an iterator. --> cannot be printed directly

# Yield runs asynchronously.


def sheep_yield(n :int):
    for i in range(n):
        yield f"{'🐑'*i}"

for s in sheep_yield(1000000):
    print(s)

# if __name__ == '__main__':
#     main()
