n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0

for i in range(n):
    if A[i] <= B[i]: ans += 1
        
print(ans)
