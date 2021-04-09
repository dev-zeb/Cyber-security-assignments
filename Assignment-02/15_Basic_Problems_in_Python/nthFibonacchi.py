
# Using Recursion
def get_fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return get_fibonacci(n-1) + get_fibonacci(n-2)

n = 7
result = get_fibonacci(n)
print('\n\n'+str(n)+"th ", "fibonacci is: ", result)