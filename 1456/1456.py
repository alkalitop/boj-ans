from math import log, ceil, floor

a, b= map(int, input().split())

arr = [0]*(10**7+1)
c = 0
for i in range(2, 10**7+1):
    if i > b: break
    if arr[i]: continue
    for j in range(1, (10**7)//i+1):
        if j > b: break
        arr[i*j] = 1
    c += floor(log(b, i)) - max(2, ceil(log(a, i))) + 1
    
print(c)
