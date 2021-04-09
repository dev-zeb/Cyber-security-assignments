
def is_leap(year):
    leap = False
    # Write your logic here
    if year%4 == 0:
        if year%100 == 0 and year%400 != 0:
            leap = False
        else:
            leap = True
    return leap

y = range(1990, 2000, 1)
for i in y:
    print(i, "is leap year: ", is_leap(i))