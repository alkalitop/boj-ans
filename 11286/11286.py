import heapq as hp
import sys
input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    x = int(input())
    if x != 0:
        hp.heappush(heap, (abs(x), x))
    else:
        if len(heap) > 0:
            print(hp.heappop(heap)[1])
        else:
            print(0)
