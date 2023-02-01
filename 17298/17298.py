n = int(input())
ret = [None]*n

A = list(map(int, input().split()))

idx = []

for i in range(n):
    while len(idx) > 0 and A[idx[-1]] < A[i]:
        ret[idx.pop()] = A[i]
    idx.append(i)
    
for j in idx:
    ret[j] = -1
    
print(*ret)
