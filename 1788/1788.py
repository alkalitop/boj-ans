n = int(input())
D = 1000000000

def f(k):
    p, q = (0, 1)
    if k < 2: return k
    for i in range(k-1): p, q = (q%D, (p+q)%D)
    return q
    
if n == 0:
    print(0)
    print(0)
else:
    print(-1 if n%2 < 1 and n < 0 else 1)
    print(f(abs(n)))
