from decimal import *
getcontext().prec = 1001
a, b = map(Decimal, input().split())
res = a/b
print(f'{res:f}')
