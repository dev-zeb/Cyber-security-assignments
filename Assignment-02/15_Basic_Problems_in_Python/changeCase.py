

def change_cases(string):
    changed_string = ""
    for i in string:
        if i.isalpha() == True:
            if i >='A' and i <= 'Z':
                ch = chr(ord(i)+32)
                changed_string += ch
            else:
                ch = chr(ord(i)-32)
                changed_string += ch
        else:
            changed_string += i

    return changed_string

string = "a CamEl cASed SEnTEnce"
result = change_cases(string)
print("\n\n" + string + " <-> " + result)