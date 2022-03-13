import sys
N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split(' ')))
M = max(score)
ssum = 0
for i in range(0, N):
    ssum = ssum + score[i]/M*100
print(ssum/N)
