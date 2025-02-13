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

is_prime = ettinc(318137)
prime = [0]
for p in range(318138):
    if is_prime[p]:
        prime.append(p)
        
for _ in range(int(input())):
    print(prime[prime[int(input())]])
    
