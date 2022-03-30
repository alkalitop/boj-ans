K = int(input())
for i in range(0, K):
    inp = list(map(int, input().split()))
    hc = inp[0]
    score = sorted(inp[1:])
    gap = []
    for j in range(0, hc-1):
        gap.append(abs(score[j+1]-score[j]))
    print('Class %d' % (i+1))
    print('Max %d, Min %d, Largest gap %d' % (max(score), min(score), max(gap)))
