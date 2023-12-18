import sys
from collections import deque

input = sys.stdin.readline

q = deque()

for _ in range(int(input())):
    s = input().split()
    if s[0] == 'push':
        q.append(s[1])
    if s[0] == 'pop':
        print(q.popleft() if len(q) else -1)
    if s[0] == 'size':
        print(len(q))
    if s[0] == 'empty':
        print(0 if len(q) else 1)
    if s[0] == 'front':
        print(q[0] if len(q) else -1)
    if s[0] == 'back':
        print(q[-1] if len(q) else -1)
