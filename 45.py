def sumarray(arr):
    sum = 0
    for num in arr:
        if type(num) == list:
           num = sumarray(num)
        sum += num
    return sum

print(sumarray([1, 2, [15, [23], [5, 12]], [100]]))