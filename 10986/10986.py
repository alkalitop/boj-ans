from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0

S = [0]*n
S[0] = A[0] % m
if S[0] == 0:
    cnt += 1

for i in range(1, n):
    S[i] = (S[i-1] + A[i]) % m
    if S[i] == 0:
        cnt += 1
    
S.sort()

comb2 = lambda z: z*(z-1)//2

for k in set(S):
    cnt += comb2(bisect_right(S, k) - bisect_left(S, k))

print(cnt)
