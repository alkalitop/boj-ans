N = int(input())
digit = len(str(N))
def round_int (x):
    n = int(x)
    a = x - n
    if a < 0.5:
        return n
    else:
        return n+1
for i in range(1, digit):
    N = int((10**i)*round_int(N/(10**i)))
print(int(N))
