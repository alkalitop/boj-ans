from collections import deque
import sys
n = int(sys.stdin.readline())

deq = deque([i for i in range(1, n+1)])

while len(deq) > 1:
    deq.popleft()
    if len(deq) == 1:
        break
    top = deq.popleft()
    deq.append(top)

print(list(deq)[0])
