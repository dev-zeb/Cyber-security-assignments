
def to_Seconds(h=0, m=0, s=0):
    total_seconds = s
    total_seconds += m*60
    total_seconds += h*3600

    return total_seconds
hours = 1
minutes = 54
seconds = 32
total_seconds = to_Seconds(hours, minutes, seconds)
print(str(hours) + 'h ' + str(minutes) + 'm ' + str(seconds) + 's = ' + str(total_seconds) + " Seconds")