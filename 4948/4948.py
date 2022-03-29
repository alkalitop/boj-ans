import sys

def BP (n):
    uf = [1]*(2*n+1)
    count = 0
    p = 2
    while p <= 2*n:
        if uf[p]:
            rc = (2*n)//p
            for i in range(1, rc+1):
                uf[p*i] = 0
            if p > n:
                count += 1
        else:
            p += 1
    return count

N = int(sys.stdin.readline())
while N:
    print(BP(N))
    N = int(sys.stdin.readline())
