import sys
input = sys.stdin.readline

def m2x2_mul (A, B):
    return [ [ A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1] ],
            [ A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1] ] ]
    
def m2x2_pow (A, n, p=0):
    if n == 1: return A
    t = m2x2_pow(A, n//2, p)
    A_ = None
    if n % 2 == 1:
        A_ = m2x2_mul(m2x2_mul(t, t), A)
    else:
        A_ = m2x2_mul(t, t)
    if p:
        A_[0][0] %= p
        A_[0][1] %= p
        A_[1][0] %= p
        A_[1][1] %= p
    return A_

def F (n, p=0):
    if n == 0: return 0
    f = ((1, 1), (1, 0))
    return m2x2_pow(f, n, p)[0][1]
    
for i in range(int(input())):
    a, b = map(int, input().split())
    print(a, F(b % (15*(10**8)), 10**9))
