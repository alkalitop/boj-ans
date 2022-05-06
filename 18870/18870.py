import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A2 = sorted(list(set(A)))

conc = {}
for i in range(len(A2)):
    conc[A2[i]] = str(i)

res = ''
for v in A:
    res += conc[v] + ' '

print(res.rstrip())
