def longestword(string):
    string = string.split(' ')
    great = string[0]
    for word in string:
        if len(great) < len(word):
            great = word
    return great

print(longestword("Youmbi Leo Lordson"))
