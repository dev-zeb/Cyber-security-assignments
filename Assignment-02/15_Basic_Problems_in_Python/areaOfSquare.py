
def areaOfSquare(length):
    return length * length
    
nums = [3, 5, 7, 9]
print('\n\n')
for n in nums:
    result = round(areaOfSquare(n), 2)
    print("Area of Square with length ", n, " : ", result)