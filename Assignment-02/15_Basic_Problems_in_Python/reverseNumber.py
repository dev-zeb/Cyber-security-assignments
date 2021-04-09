
def reverseNumber(n):
    result = n%10
    n //= 10
    while n > 0:
        result = result*10 + (n%10)
        n //= 10
    return result
     

n = 7456987
result = reverseNumber(n)
print('\n\nReverse of '+str(n)+" is: ", result)
