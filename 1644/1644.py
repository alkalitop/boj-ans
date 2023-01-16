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

if n == 1:
    
    print(0)
    
else:

    prime = eratosthenes(n)

    i = len(prime)-1
    j = i

    cnt = 0

    s = prime[-1]

    while 0 <= i <= j:
        if s == n:
            cnt += 1
            i -= 1
            s += prime[i]
        elif s > n:
            s -= prime[j]
            j -= 1
        elif s < n:
            i -= 1
            if i < 0: break
            s += prime[i]
        
    print(cnt)
    
