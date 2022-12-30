def strtoascii(string):
    a = 0
    string = list(string)
    for i in string:
        string[a] = ord(i)
        a += 1
    return string

print(strtoascii("I love yu"))


