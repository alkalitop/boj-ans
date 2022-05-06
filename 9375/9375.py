import sys
input = sys.stdin.readline

for i in range(int(input())):
    A = {}
    for j in range(int(input())):
        kind = input().split()[1]
        if not kind in A:
            A[kind] = 1
        A[kind] += 1
    res = 1
    for k in list(A.keys()):
        res *= A[k]
    print(res-1)
