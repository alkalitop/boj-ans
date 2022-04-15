import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
deq = deque()

for i in range(k):
    n = int(input())
    if n:
        deq.append(n)
    else:
        deq.pop()

print(sum(list(deq)))
