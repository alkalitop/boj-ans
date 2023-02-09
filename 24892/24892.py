n = int(input())
a, b = map(int, input().split())

c = b-a

p = 10**9+7

def pow (a, x):
    if x == 0:
        return 1
    t = pow(a, x//2)
    if x % 2 == 1:
        return t*t*a % p
    else:
        return t*t % p

u = pow(c,3)
v = (p+1-pow(n**2,p-2))%p
print((((u*v)%p)*166666668)%p)
