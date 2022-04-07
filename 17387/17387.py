cross_product = lambda A, B, C: A[0]*B[1]+B[0]*C[1]+C[0]*A[1]-(B[0]*A[1]+C[0]*B[1]+A[0]*C[1])
def CCW (A, B, C):
    cp = cross_product(A, B, C)
    if cp > 0:
        return 1
    elif cp < 0:
        return -1
    else:
        return 0

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

P1 = (x1, y1)
P2 = (x2, y2)
P3 = (x3, y3)
P4 = (x4, y4)

C123 = CCW(P1, P2, P3)
C124 = CCW(P1, P2, P4)
C341 = CCW(P3, P4, P1)
C342 = CCW(P3, P4, P2)

lic = lambda a, b, c, d: (min(a, b) <= max(c, d)) and (min(c, d) <= max(a, b))

if not (C123*C124 or C341*C342):
    if lic(x1, x2, x3, x4) and lic(y1, y2, y3, y4):
        print(1)
    else:
        print(0)
elif C123*C124 <= 0 and C341*C342 <= 0:
    print(1)
else:
    print(0)
