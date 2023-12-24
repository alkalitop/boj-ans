MRPT_PRIME = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

def mrpt_seg (n, a):
    d = n-1
    r = 0
    while -~n & 1:
        d >>= 1
        r += 1
    t = pow(a, d, n)
    if t == 1 or t == n-1:
        return 1
    for i in range(r-1):
        t = pow(t, 2, n)
        if t == n-1:
            return 1
    return 0

def mrpt (n):
    tmp = 0
    if n in MRPT_PRIME:
        return 1
    if -~n & 1:
        return 0
    for a in MRPT_PRIME:
        if not mrpt_seg(n, a):
            return 0
    return 1
