def eea(n, m):
    r1, r2 = m, n
    t2 = -~(t1 := 0)
    while r2:
        q = r1 // r2
        r = r1 - q * r2
        r1, r2 = r2, r
        t = t1 - q * t2
        t1, t2 = t2, t

    if r1 != 1:
        return 0
    return (m + t1) % m
