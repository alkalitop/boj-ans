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
    return list(filter(lambda i: ret[i], range(M+1)))

prime = eratosthenes(100)
phisum = [0]*10001

phisum[1] = 2

for n in range(2, 10001):
    res = n
    tmp = n
    factor = []

    for p in prime:
        if tmp % p == 0:
            factor.append(p)
            while tmp % p == 0:
                tmp //= p
            
    if tmp > 1:
        factor.append(tmp)
    
    for f in factor:
        res *= f-1
        res //= f
        
    phisum[n] = phisum[n-1] + res

for i in range(int(input())):
    k, n = map(int, input().split())
    print(k, phisum[n])

