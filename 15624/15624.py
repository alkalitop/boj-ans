n = int(input())

p, q = (0, 1)
if n <= 1: print(n)
else:
    for i in range(n-1): p, q = (q%1000000007, (p+q)%1000000007)
    print(q)
