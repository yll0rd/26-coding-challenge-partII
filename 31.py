"""
def countwords(string):
    count=0
    for i in string:
        count+=1
    return f"{count} words"
"""
        
def countwords(string):
    return f"{len(string)} words"
    
print(countwords("Faith"))
    