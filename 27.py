def getdistinctelements(arr):
    liste = []
    for num in arr:
        if arr.count(num) == 1:
            liste.append(num)
    return liste

print(getdistinctelements([1,2,3,3,4]))