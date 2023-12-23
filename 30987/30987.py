x1, x2 = map(int, input().split())
a, b, c, d, e = map(int, input().split())

p = a//3
q = (b-d)//2
r = c-e

f = lambda x: p*x**3 + q*x**2 + r*x
print(f(x2)-f(x1))
