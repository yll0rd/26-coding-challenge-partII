from re import I


n = 70
ans = 1
for i in range(n,1,-1):
    ans *= i
print(round(ans))