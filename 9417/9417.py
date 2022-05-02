import sys
from math import gcd
input = sys.stdin.readline

for _ in range(int(input())):
    A = list(map(int, input().split()))
    m = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                m = max(m, gcd(A[i], A[j]))
    print(m)
	
