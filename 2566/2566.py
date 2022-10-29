import sys
input = sys.stdin.readline

v = 0
p = (1, 1)

for i in range(9):
    seq = list(map(int, input().split()))
    for j in range(9):
        if seq[j] > v:
            v = seq[j]
            p = (i+1, j+1)

print(v)
print(p[0], p[1])
