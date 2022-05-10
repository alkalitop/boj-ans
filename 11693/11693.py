res = 1
n, m = map(int, input().split())
p = 1000000007

def dcpow (a, n, p):
    if n == 0:
        return 1
    t = dcpow(a, n//2, p)
    if n % 2 == 1:
        return t*t*a % p
    else:
        return t*t % p

for i in range(2, n):
	if n == 1 or i*i > n: break
	c = 0
	while n % i == 0:
		c += 1
		n //= i
	if c == 0: continue
	res *= ((dcpow(i % p, c*m + 1, p) - 1) % p) * dcpow((i - 1) % p, p - 2, p)
	res %= p

if n > 1:
	res *= ((dcpow(n % p, m + 1, p) - 1) % p) * dcpow((n - 1) % p, p - 2, p)

print(res % p)
