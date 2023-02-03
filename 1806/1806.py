n, s = map(int, input().split())
A = list(map(int, input().split()))

i = 0
j = 0

p = A[0]
L = n+1

while i <= j < n:
    if p < s:
        j += 1
        if j == n: break
        p += A[j]
    else:
        L = min(L, j-i+1)
        p -= A[i]
        i += 1
        
print(L if L <= n else 0)
