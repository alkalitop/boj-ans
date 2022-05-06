import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
dA = [0]

acc = 0
for v in A:
    acc += v
    dA.append(acc)

for _ in range(m):
    i, j = map(int, input().split())
    print(dA[j] - dA[i-1])
