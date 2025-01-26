def mod_inverse(n, m):
    r1, r2 = m, n
    t2 = -~(t1 := 0)
    while r2:
        s = r1 // r2
        r = r1 - s * r2
        r1, r2 = r2, r
        t = t1 - s * t2
        t1, t2 = t2, t

    return 0 if r1 != 1 else (m + t1) % m

def ettinc(M):
    ret = [1]*(M+1)
    ret[0], ret[1] = 0, 0
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

is_prime = ettinc(int(10**4.5))

def factorize(n):
    for p in range(2, len(is_prime)):
        if (not is_prime[p]) or n % p: continue
        return (p, n//p)

def mmi(e, k):
    v = mod_inverse(1, k)
    while v % e:
        v += k
    return v // e

def decrypt(n, e, c):
    p, q = factorize(n)
    d = mmi(e, (p-1)*(q-1))
    return pow(c, d, n)
        

for i in range(int(input())):
    print(f'Data Set {i+1}:')
    print(decrypt(*map(int, input().split())))
    print()
