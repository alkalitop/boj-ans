from collections import deque

n = int(input())
d = deque(enumerate(map(int, input().split()), start=1))

r = [0]*n

for i in range(n):
    s = d.popleft()
    r[i] = s[0]
    d.rotate(-s[1] + (1 if s[1] > 0 else 0))
    
print(*r)
