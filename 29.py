def isprime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

i = 2
j = 3
count = 0
while count<100:
    if isprime(j):
        print(j,"-",i,"=",j-i)
        count += 1
        i = j
    j += 1