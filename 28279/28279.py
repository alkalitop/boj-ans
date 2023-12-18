import sys
from collections import deque

input = sys.stdin.readline

deq = deque()

for _ in range(int(input())):
    s = input().split()
    c = int(s[0])
    x = int(s[1]) if len(s) > 1 else 0
    if c == 1:
        deq.appendleft(x)
    if c == 2:
        deq.append(x)
    if c == 3:
        print(deq.popleft() if len(deq) else -1)
    if c == 4:
        print(deq.pop() if len(deq) else -1)
    if c == 5:
        print(len(deq))
    if c == 6:
        print(0 if len(deq) else 1)
    if c == 7:
        print(deq[0] if len(deq) else -1)
    if c == 8:
        print(deq[-1] if len(deq) else -1)
