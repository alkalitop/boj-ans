from math import gcd, log2
n, d = map(int, input().split())
if n == 0:
    print(1)
    print('U')
else:
    g = gcd(n, d)
    n //= g
    d //= g
    t = d
    while t % 2 == 0:
        t //= 2
    if t != 1:
        print(-1)
    else:
        r = 'D'*int(log2(d))
        b = bin(n).split('b')[1]
        for i in range(len(b)-1, -1, -1):
            if i < len(b)-1:
                r += 'U'
            if b[i] == '1':
                r += ('R' if n > 0 else 'L')
        if len(r) > 1000:
            print(-1)
        else:
            print(len(r))
            print(r)
