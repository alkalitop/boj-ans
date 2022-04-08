import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

input()
A = sorted(list(map(int, input().split())))
input()
for s in input().split():
    t = int(s)
    print(1 if bisect_left(A, t) < bisect_right(A, t) else 0)
