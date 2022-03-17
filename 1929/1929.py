M, N = map(int, input().split())
uf = [1]*(N+1)
primes = []

p = 2
while p <= N:
    if uf[p]:
        rc = N//p
        for i in range(1, rc+1):
            uf[p*i] = 0
        if p >= M:
            print(p)
    else:
        p += 1
