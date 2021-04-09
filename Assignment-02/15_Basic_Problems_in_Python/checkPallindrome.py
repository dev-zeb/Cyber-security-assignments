
def check_pallindrome(string):
    i = 0
    j = len(string) - 1

    while i != j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True

str = "HowoH"
result = check_pallindrome(str)
print("\n\nFor ", str,  ": ", result)