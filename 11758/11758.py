crossProduct = lambda A, B, C: A[0]*B[1]+B[0]*C[1]+C[0]*A[1]-(B[0]*A[1]+C[0]*B[1]+A[0]*C[1])
def setPoint(): 
    return tuple(map(int, input().split()))
P = setPoint()
Q = setPoint()
R = setPoint()
cp = crossProduct(P, Q, R)
if not cp:
    print(0)
else:
    print(cp//abs(cp))
