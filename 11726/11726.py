n = int(input())
D = 10007

def f(k):
    p, q = (0, 1)
    if k < 2: return k
    for i in range(k-1): p, q = (q%D, (p+q)%D)
    return q
    
print(f(n+1))
