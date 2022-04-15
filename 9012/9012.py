from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    brs = list(input().strip())
    deq = deque()
    end = 0
    for s in brs:
        if s == '(':
            deq.append(1)
        if s == ')':
            if len(deq) == 0:
                print('NO')
                end = 1
                break
            else:
                deq.pop()
    if len(deq) > 0:
        print('NO')
        end = 1
    if not end:
        print('YES')
