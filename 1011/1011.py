import sys
import math
input = sys.stdin.readline
f = lambda n: math.floor(math.sqrt(4*n+1))

for i in range(int(input())):
    a, b = map(int, input().split())
    print(f(b-a-1))
