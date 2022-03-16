import math
A, B, Z = map(int, input().split(' '))
print(math.ceil((Z-A)/(A-B))+1)
