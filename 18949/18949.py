from decimal import *

getcontext().prec = 100
sqrt = getcontext().sqrt

a = Decimal(input() + '.' + '0'*100)

S1 = getcontext().power( (2*a+1)*(2*a+1) - 4*a*a , Decimal('1.5'))/6

g = lambda x: -x*( 3*a*a - 3*a*(x+1) + x*x + 2*sqrt(x) )/3

x1 = Decimal('0.5')*( 2*a + sqrt(4*a-3) - 1 )
x2 = Decimal('0.5')*( 2*a - sqrt(4*a+1) + 1 )

S2 = g(x2) - g(x1)

print(round(2*(S1+S2), 10))
