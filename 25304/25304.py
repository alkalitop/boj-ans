import sys
input = sys.stdin.readline

t = int(input())
s = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    s += a*b
print('Yes' if t == s else 'No')
