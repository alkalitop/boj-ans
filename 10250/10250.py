import math
T = int(input())
for i in range(0, T):
    H, W, N = map(int, input().split())
    r = math.ceil(N/H);
    f = N%H
    print(f*100+r if f != 0 else H*100+r)
    
