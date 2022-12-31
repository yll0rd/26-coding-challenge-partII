def findmax(arr):
    great = arr[0]
    for num in arr[1:]:
        if type(num) == list:
           num = findmax(num)
        if great < num:
            great = num
    return great

print(findmax([1, 3, [15, [123], [5, 12]], [101]]))