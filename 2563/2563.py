import sys
input = sys.stdin.readline

bg = [None]*100
for _ in range(100):
    bg[_] = [0]*100

for _ in range(int(input())):
    p = tuple(map(int, input().split()))
    for i in range(p[1], p[1]+10):
        for j in range(p[0], p[0]+10):
            bg[i][j] = 1

print(sum(list(map(sum, bg))))
