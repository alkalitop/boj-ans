import heapq as hp
import sys
input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    x = input().strip()
    if x == '0':
        if len(heap) > 0:
            print(hp.heappop(heap)[1])
        else:
            print(-1)
    else:
        a = x.split()
        for i in range(1, int(a[0])+1):
            hp.heappush(heap, (-int(a[i]), int(a[i])))
