import math

def fracsum (A):
    d = {}
    size = len(A)
    
    for t in A:
        if not t in d: d[t] = 0
        d[t] += 1
    
    for k in range(2, size+1):
        a0 = -1
        ex = ''
        for i in range(k):
            ex += ' '*(4*i) + f'for a{i+1} in range(a{i}+1, size):\n'
        ex += ' '*(4*k) + 't = 0\n'
        for i in range(k):
            ex += ' '*(4*k) + f't += A[a{i+1}]\n'
        ex += ' '*(4*k) + 'if not t in d: d[t] = 0\n'
        ex += ' '*(4*k) + 'd[t] += 1\n'
        exec(ex)
    return d

n, s = map(int, input().split())
A = list(map(int, input().split()))

A1 = fracsum(A[:n//2])
A2 = fracsum(A[n//2:])

ans = A1.get(s, 0) + A2.get(s, 0)

for p in A1:
    ans += A1[p] * A2.get(s-p, 0)

print(ans)
