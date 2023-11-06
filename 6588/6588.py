import sys
input = sys.stdin.readline

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
 
d = 10**6 
prime = eratosthenes(d)

while 1:
    n = int(input())
    if not n: break
    
    t = n>>1
    p = 0
    
    for i in range(3, t+1):
        if prime[i] and prime[n-i]:
            p = i
            break
    
    if p:
        print(n, '=', p, '+', n-p)
    else:
        print("Goldbach's conjecture is wrong.")

