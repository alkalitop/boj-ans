n = int(input())

def H (m, p, q):
    r = (p+q)%4
    if r == 0: r += 2
    if m != 1:
        H(m-1, p, r)
        print(p, q)
        H(m-1, r, q)
    else:
        print(p, q)

print((1<<n)-1)
H(n, 1, 3)
