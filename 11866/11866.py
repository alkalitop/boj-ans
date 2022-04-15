from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
deq = deque([i for i in range(1, n+1)])
res = [0]*n

for i in range(n):
    for j in range(k-1):
        deq.append(deq.popleft())
    res[i] = deq.popleft()

print('<' + ', '.join(map(str, res)) + '>')
