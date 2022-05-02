from decimal import *
a, b = map(Decimal, input().split())
getcontext().prec = 10000
res = a**b
print(f'{res:f}')
