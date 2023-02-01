from decimal import getcontext, Decimal

getcontext().prec = 51
pi = Decimal('3.14159265358979323846264338327950288419716939937510')

def sin(x):
    while x < -pi:
        x += 2*pi
    while x > pi:
        x -= 2*pi

    S = x

    n = 1
    nfac = 1
    xexn = x
    sign = 1

    prev = x

    while abs(prev) > Decimal(1e-50):
        n += 2
        sign *= -1
        nfac *= n*(n-1)
        xexn *= x**2

        prev = sign*xexn/nfac

        S += prev

    return S

a, b, c = map(Decimal, input().split())

f = lambda x: a*x + b*Decimal(sin(x)) - c

_1 = Decimal('1')
p = c/a-_1
q = c/a+_1
m = (p+q)/2

while q - p > Decimal(1e-20):
    if f(m) > 0:
        q = m
        m = (p+q)/2
    elif f(m) < 0:
        p = m
        m = (p+q)/2
    else:
        m = (p+q)/2
        break

print(round(m, 6))
