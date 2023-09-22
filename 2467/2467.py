n = int(input())
A = list(map(int, input().split()))

i = 0
j = n-1

p = A[i]
q = A[j]
s = abs(p+q)

while i < j:
    r = A[i]+A[j]
    
    if r == 0:
        p = A[i]
        q = A[j]
        break
    
    if abs(r) < s:
        p = A[i]
        q = A[j]
        s = abs(p+q)
        
    if r < 0:
        i += 1
    else:
        j -= 1
 
print(p, q)
        
    
