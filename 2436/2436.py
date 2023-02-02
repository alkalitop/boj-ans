from math import gcd

a, b = map(int, input().split())
n = b//a
d = 0
for i in range(1, int(n**0.5)+1):
    if n % i == 0 and gcd(i, n//i) == 1:
        d = i
        
print(d*a, (n//d)*a)

