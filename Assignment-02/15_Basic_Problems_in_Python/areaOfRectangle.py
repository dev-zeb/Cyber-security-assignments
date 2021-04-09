
def areaOfRectangle(l, w):
    return l * w
    
lengths = [3, 5, 7, 9]
widths = [5, 7, 10, 15]
print('\n\n')
for i in range(len(lengths)):
    a = lengths[i]
    b =  widths[i]
    result = round(areaOfRectangle(a, b), 2)
    print("Area of Square with length ", a, " and width ", b, " : ", result)