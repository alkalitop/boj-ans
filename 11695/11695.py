import sys
input = sys.stdin.readline

s = 0
n, m = map(int, input().split())
for _ in range(n):
    a = sum(map(int, input().split()))
    s ^= a
print('august14' if s else 'ainta')
