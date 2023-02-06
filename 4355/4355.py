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

prime = eratosthenes(10**5)

n = int(input())
while n > 0:
    if n == 1: 
        print(0)
    else:
        tmp = n
        res = n
        factor = []

        for p in prime:
            if tmp % p == 0:
                factor.append(p)
                while tmp % p == 0:
                    tmp //= p
            
        if tmp > 1 and not tmp in factor:
            factor.append(tmp)
    
        for f in factor:
            res *= f-1
            res //= f
        
        print(res)
    n = int(input())

