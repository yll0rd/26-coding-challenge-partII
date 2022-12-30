from math import sqrt

n=500
a= (1+sqrt(5))**n - (1-sqrt(5))**n
b= sqrt(5)*2**n
print(f"{round(a/b)}")