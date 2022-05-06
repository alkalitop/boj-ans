import heapq as hp
import sys
input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    x = int(input())
    if x > 0:
        hp.heappush(heap, x)
    else:
        if len(heap) > 0:
            print(hp.heappop(heap))
        else:
            print(0)
