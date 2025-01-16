from math import gcd, ceil

def euc(a, b):
    r = [0] * 2
    if not b:
        r[0] = 1
        r[1] = 0
        return r
    q = a // b
    v = euc(b, a % b)
    r[0] = v[1]
    r[1] = v[0] - v[1]*q
    return r

a, b, c = map(int, input().split())
if not c:
    print('NO' if a and b else 'YES')
else:
    if (not a) and (not b):
        print('NO')
    elif (not a) and b:
        print('NO' if c % b else 'YES')
    elif a and (not b):
        print('NO' if c % a else 'YES')
    else:
        if c % gcd(a, b):
            print('NO')
        else:
            d = gcd(a, b)
            x, y = map(lambda t: t*c//d, euc(a, b))
            u = a//d
            v = b//d
            if x >= 0 and y >= 0:
                print('YES')
            elif x >= 0 and y < 0:
                k = ceil(-y / u)
                x -= k*v
                y += k*u
                while x >= 0:
                    if gcd(x, y) == 1:
                        print('YES')
                        break
                    else:
                        x -= v
                        y += u
                else:
                    print('NO')
            elif x < 0 and y >= 0:
                k = ceil(-x / v)
                x += k*v
                y -= k*u
                while y >= 0:
                    if gcd(x, y) == 1:
                        print('YES')
                        break
                    else:
                        x += v
                        y -= u
                else:
                    print('NO')
