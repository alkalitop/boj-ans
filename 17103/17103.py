def eratosthenes(M):
    ret = [1]*(M+1)
    ret[0], ret[1] = (0, 0)
    p = 2
    while p in range(int(M**0.5)+1):
        if ret[p]:
            ret[p] = 1
            i = 2
            while p*i <= M:
                ret[p*i] = 0
                i += 1
        p += 1
    return ret

prime = eratosthenes(10**6+1)

for _ in range(int(input())):
    n = int(input())
    c = 0
    for i in range(2, n//2+1):
        if prime[i] and prime[n-i]:
            c += 1
    print(c)
