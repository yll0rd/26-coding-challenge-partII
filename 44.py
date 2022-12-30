from math import pow

def bintodec(string):
    l = len(string)
    sum = 0
    for num in string:
        sum += int(num)*pow(2, l-1)
        l -= 1
    return round(sum)


print(bintodec("100"))