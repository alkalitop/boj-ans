from math import log2

n = int(input())
print(int(log2(n))+(2 if n&~-n else 1) if n else 0)
