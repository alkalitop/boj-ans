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

n = int(input())
res = n

prime = eratosthenes(int(n**0.5))
factor = []

for p in prime:
    if n % p == 0:
        factor.append(p)
        while n % p == 0:
            n //= p
            
if n > 1:
    factor.append(n)
    
for f in factor:
    res *= f-1
    res //= f
        

print(res)
