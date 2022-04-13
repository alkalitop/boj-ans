import sys
input = sys.stdin.readline

n = int(input())
scores = [0]*n
for i in range(n):
    scores[i] = float(input())
scores.sort()

for i in range(7):
    print('%.3f' % scores[i])
