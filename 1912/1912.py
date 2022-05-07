import heapq as hp
n = int(input())

A = list(map(int, input().split()))
dA = []
dA.append(A[0])

ms = A[0]
prev = A[0]
for i in range(1, n):
    curr = prev + A[i]
    ms = max(ms, curr-dA[0], curr)
    hp.heappush(dA, curr)
    prev = curr
    
print(ms)
