d = 10**9+7

def m2x2_mul (A, B):
    return [ [ A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1] ],
            [ A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1] ] ]
    
def m2x2_pow (A, n):
    if n == 1: return A
    t = m2x2_pow(A, n//2)
    A_ = None
    if n % 2 == 1:
        A_ = m2x2_mul(m2x2_mul(t, t), A)
    else:
        A_ = m2x2_mul(t, t)
    A_[0][0] %= d
    A_[0][1] %= d
    A_[1][0] %= d
    A_[1][1] %= d
    return A_

def F(k):
    if k == 1: return 3
    if k == 2: return 11
    X = ((4, d-1), (1, 0))
    Y = m2x2_pow(X, k-1)
    return 3*Y[0][0]+Y[0][1]

n = int(input())

if n % 2:
    print(0)
else:
    print(F(n>>1)%d)
