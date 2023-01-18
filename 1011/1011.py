import math

for i in range(int(input())):
    a, b = map(int, input().split())
    print(math.sqrt(((b-a-1)<<2)+1))
