from math import ceil,sqrt
n = int(input())
print(2*ceil(2*sqrt(n))-4 if n > 4 else 4)
