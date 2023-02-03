m = 10**9+7
D = [0]*(10**5+1)
D[1] = 0
D[2] = 1

n = int(input())
fac = 1

if n == 1:
    print(0)
elif n == 2:
    print(2)
else:
    fac = 2
    for i in range(3, n+1):
        D[i] = (i-1)*(D[i-1]+D[i-2]) % m
        fac *= i
        fac %= m
    print((D[n]*fac)%m)
