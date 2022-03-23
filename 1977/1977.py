import math
M = int(input())
N = int(input())
CE = []
for n in range(M, N+1):
    if math.sqrt(n) == int(math.sqrt(n)):
        CE.append(n)
    else:
        pass
if not len(CE):
    print(-1)
else:
    print(sum(CE))
    print(min(CE))
