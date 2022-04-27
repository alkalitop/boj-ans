n = int(input())

A = [1]*(n+1)
for i in range(4, n+1):
    A[i] = A[i-1] + A[i-3]
print(A[n])
