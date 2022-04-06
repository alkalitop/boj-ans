import math

p1, q1 = map(int, input().split())
p2, q2 = map(int, input().split())

n = p1*q2 + p2*q1
d = q1*q2

G = math.gcd(n, d)
print(n//G, d//G)
