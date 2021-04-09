

def time_break_down(total_seconds):
    hours = total_seconds//3600
    minutes = (total_seconds%3600)//60
    seconds = total_seconds%60

    return hours, minutes, seconds

total_seconds = 6872
hours, minutes, seconds = time_break_down(total_seconds)
print(str(total_seconds) + " Seconds = " + str(hours) + 'h ' + str(minutes) + 'm ' + str(seconds) + 's')
    