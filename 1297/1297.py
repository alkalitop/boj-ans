import math
D, H, W = map(int, input().split())
r = math.sqrt((D**2)/(H**2+W**2))
print(math.floor(H*r), math.floor(W*r))
