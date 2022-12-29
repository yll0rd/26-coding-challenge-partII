from re import I


def isprime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
       
count = i = sum = 0
while count < 100:
    if isprime(i) == True:
        sum += i
        count += 1
    i += 1
print("The sum of the first 100 prime numbers are:",sum)