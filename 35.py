def csvto2d(string):
    liste = []
    a = 0
    string = string.split(",")
    for i in string:
        liste.insert(a, list(i))
        a += 1
    return liste

print(csvto2d("leo,lordson,youmbi"))   
