def sumstring(n):
    sum=0
    n=n.split(',')
    for i in n:
        sum+=int(i)
    return sum
   
print(sumstring("1,2,3,4"))