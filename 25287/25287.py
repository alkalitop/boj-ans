import sys
input = sys.stdin.readline

L = lambda x,n: min(x, n+1-x)

for i in range(int(input())):
    n = int(input())
    p = [*map(lambda t: L(int(t), n), input().split())]
    for i in range(1, n):
        if p[i-1] > p[i]:
            p[i] = n+1-p[i]
        if p[i-1] > p[i]:
            print('NO')
            break            
    else:
        print('YES')
