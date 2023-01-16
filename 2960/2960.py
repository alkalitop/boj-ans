n, k = map(int, input().split())
rm = []

def eratosthenes(M):
    ret = [1]*(M+1)
    ret[0], ret[1] = (0, 0)
    p = 2
    while p in range(M+1):
        if ret[p]:
            ret[p] = 1
            rm.append(p)
            i = 2
            while p*i <= M:
                if ret[p*i]:
                    rm.append(p*i)
                    ret[p*i] = 0
                i += 1
        p += 1
    return list(filter(lambda i: ret[i], range(M+1)))
    
eratosthenes(n)

print(rm[k-1])
