import math
C = math.comb

n = int(input())//2
m = 987654321

def cat (k):
    return C(2*k, k)//(k+1) # Catalan number

print(cat(n)%m)
