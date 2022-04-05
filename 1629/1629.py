A, B, C = map(int, input().split())

def dcpow (a, x):
    if x == 0:
        return 1
    t = dcpow(a, x//2)
    if x % 2 == 1:
        return t*t*a % C
    else:
        return t*t % C
    
print(dcpow(A, B) % C)
