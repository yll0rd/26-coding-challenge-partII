"""
def liststring(string):
    return list(string)
"""
    
def liststring(string):
    liste = []
    for i in string:
        liste.append(i)
    return list(string)
    
print(liststring("Okay bro"))