def getcharfreq(string):
    liste = []
    li = []
    string = list(string)
    for letter in string:
        if ord(letter) not in range(65,91) and ord(letter) not in range(97,123):
            continue
        if letter not in li:
            liste.append([letter, string.count(letter)])
        li.append(letter)

    return liste

print(getcharfreq("My name is Youmbi Leo"))

