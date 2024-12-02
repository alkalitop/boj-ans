from decimal import *
getcontext().prec = 36
n = Decimal(input())
x = Decimal(input())

m = n - n*x*Decimal('0.01')
print(100*(n/m-1))
