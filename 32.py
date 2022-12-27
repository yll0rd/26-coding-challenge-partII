def capital(string):
    j = 0
    string = string.split(' ')
    for i in string:
        string[j] = i.capitalize()
        j += 1
    string = ' '.join(string)
    return string

print(capital("my name is youmbi leo"))