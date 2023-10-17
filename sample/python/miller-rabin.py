def mrpt_seg (n, a):
    d = ~-n
    r = 0
    while -~n & 1:
        d >>= 1
        r += 1
    t = pow(a, d, n)
    if t == 1 or t == ~-n:
        return 1
    for i in range(~-r):
        t = pow(t, 2, n)
        if t == ~-n:
            return 1
    return 0
	
def mrpt (n):
    tmp = 0
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if n in prime:
        return 1
    if -~n & 1:
        return 0
    for a in prime:
        if not mrpt_seg(n, a):
            return 0
    return 1
