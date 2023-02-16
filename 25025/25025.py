n, p = map(int, input().split())
A = list(map(int, input().split()))
A_ = lambda z: A[n-z]
B = [0]*p

for i in range(n+1):
    B[i % (p-1)] += A_(i) % p
    B[i % (p-1)] %= p

def modmul (a, b, p):
    return ((a%p)*(b%p))%p

for x in range(p):
    if x == 0:
        print(A[n] % p)
    else:
        r = 0
        y = 1
        for j in range(p):
            r += modmul(B[j], y, p)
            y *= x
            y %= p
        print(r % p)
