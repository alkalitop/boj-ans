def pf (n):
    factor = {}
    for i in range(2, n//2+1):
        while n % i == 0:
            if not i in factor: factor[i] = 0
            factor[i] += 1
            n //= i
        if n > 1: factor[n] = 1
    return factor
