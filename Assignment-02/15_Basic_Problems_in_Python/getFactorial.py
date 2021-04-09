
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
    
nums = [3, 4, 5, 6, 7, 10]
print('\n\n')
for n in nums:
    result = factorial(n)
    print("Factorial of ", n, " is: ", result)