import sys

input = sys.stdin.readline

def stb (s):
    return (8 if s[0] == 'E' else 0) + (4 if s[1] == 'S' else 0) + (2 if s[2] == 'T' else 0) + (1 if s[3] == 'J' else 0)

bits = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

for _ in range(int(input())):
    m = 12
    if int(input()) > 32:
        input()
        print(0)
        continue
    A = list(map(stb, input().split()))
    for i in range(len(A)-2):
        for j in range(i+1, len(A)-1):
            for k in range(j+1, len(A)):
                c = bits[A[i]^A[j]]+bits[A[j]^A[k]]+bits[A[k]^A[i]]
                m = min(c, m)
    print(m)
