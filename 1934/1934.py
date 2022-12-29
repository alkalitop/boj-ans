import math
for i in range(int(input())):
    A, B = map(int, input().split())
    print(A*B//math.gcd(A, B))
