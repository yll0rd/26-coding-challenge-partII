
def sumstring(n):
    sum=0
    n=n.split(',')
    print(n)
    for i in n:
        sum+=int(i)
    return sum

"""    
def sumstring(n):
   liste=[]
   sum=0
   for i in n:
       if i == ',':
           continue
       liste.append(i)
   print(liste)
   for i in liste:
       sum+=int(i)
   return sum
"""
       
   
print(sumstring("1,2,3,4,5"))