
import math

def length_of_number(number):
    return math.floor(math.log(number, 10))+1

n = 3563077
numberLength = length_of_number(n)
print("\n\nLength of " + str(n) + " <-> " + str(numberLength))
    