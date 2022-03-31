import sys
T = int(sys.stdin.readline())

seq = [0]*101
seq[1] = 1
seq[2] = 1
seq[3] = 1

def f(n):
    if not seq[n]:
        seq[n] = f(n-2) + f(n-3)
    return seq[n]

for i in range(0, T):
    N = int(sys.stdin.readline())
    print(f(N))
