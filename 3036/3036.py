from math import gcd

n = int(input())
A = list(map(int, input().split()))

for i in range(1, len(A)):
    G = gcd(A[0], A[i])
    print(f'{A[0]//G}/{A[i]//G}')
