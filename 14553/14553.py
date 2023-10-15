n = int(input())
m = 10**9+9

a = [0]*-~n
b = [0]*-~n
c = [0]*-~n
d = lambda k: a[k]+b[k]+c[k]

Sa = [0]*-~n
Sc = [0]*-~n

a[1] = 1
b[1] = 1
c[1] = 1

Sc[0] = 1

for i in range(2, n+1):
    a[i] = (d(i-1)+Sc[i-2])%m
    b[i] = d(i-1)%m
    c[i] = (d(i-1)+Sa[i-2])%m
    Sa[i-1] = (Sa[i-2]+a[i-1])%m
    Sc[i-1] = (Sc[i-2]+c[i-1])%m

print(a[n])
