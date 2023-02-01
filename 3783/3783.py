from decimal import *

getcontext().prec = 1000
t = Decimal('1')/Decimal('3')
for i in range(int(input())):
    a = round(Decimal(Decimal(input().rstrip()+'.'+'0'*10)**t),500)
    print(Decimal(a).quantize(Decimal('.'+('0'*9)+'1'), rounding=ROUND_DOWN))
