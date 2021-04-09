
import math

PI = math.pi

def areaOfCircle(radius):
    return PI * radius * radius
    
nums = [3, 5, 7, 9]
print('\n\n')
for n in nums:
    result = round(areaOfCircle(n), 2)
    print("Area of Circle with radius ", n, " : ", result)