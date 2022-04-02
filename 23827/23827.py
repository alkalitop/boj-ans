N = int(input())
A = list(map(int, input().split()))
sumA = sum(A)
result = 0
for i in range(0, N): 
    cur = A[N-1-i]
    sumA -= cur
    result += sumA*cur
print(result % 1000000007)
