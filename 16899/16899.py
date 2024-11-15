import sys
input = sys.stdin.readline

def sxor(x):
    if x % 4 == 1:
        return 1
    elif x % 4 == 2:
        return x+1
    elif x % 4 == 3:
        return 0
    else:
        return x

n = int(input())
s = 0

for i in range(n):
    x, m = map(int, input().split())
    s ^= sxor(x+m-1)^sxor(x-1)
        
print('koosaga' if s else 'cubelover')
