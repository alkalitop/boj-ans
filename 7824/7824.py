import sys
input = sys.stdin.readline

def g(x):
    return g(x >> 1) if x & 1 else x >> 1

for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    s = 0
    for i in range(n):
        s ^= g(a[i])
    print('YES' if s else 'NO')
          
