
import math
def checkPrime(n):
    i = 2
    root = math.floor(math.sqrt(n))
    while i <= root:
        if n%i == 0:
            return False
        i += 1
    return True

nums = [5151512515524, 7, 56963]
print('\n\n')
for n in nums:
    result = checkPrime(n)
    print(str(n)+" is Prime?:", result)
