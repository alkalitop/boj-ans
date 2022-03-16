T = int(input())
def hc (k, n):
    head = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    head2 = head[:]
    for i in range(0, k):
        for j in range(1, n+1):
            for z in range(1, j):
                head2[j] += head[z]
        head = head2[:]
    return head2[n]

for i in range(0, T):
    k = int(input())
    n = int(input())
    print(hc(k, n))
