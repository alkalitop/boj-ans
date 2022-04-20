import math
n, m, k = map(int, input().split())
if k == 0:
    print(math.comb(n+m-2, n-1))
else:
    Xa = k%m-1
    Ya = math.ceil(k/m)-1
    if Xa < 0: Xa += m
    Xb = m-Xa-1
    Yb = n-Ya-1
    print(math.comb(Xa+Ya, Xa)*math.comb(Xb+Yb, Xb))
