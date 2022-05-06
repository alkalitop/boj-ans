n = int(input())
D = 10007

def f(k):
    p, q = (1, 3)
    if k < 3: return (1, 3, 5)[k]
    for i in range(k-1): p, q = (q%D, (2*p+q)%D)
    return q
    
print(f(n-1))
