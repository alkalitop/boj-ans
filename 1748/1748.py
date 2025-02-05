from math import log10
n = int(input())
b = int(log10(n))
print(n*(b+1) - (10**b-1)*10//9 + b)
