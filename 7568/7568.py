import sys
input = sys.stdin.readline

n = int(input())
arr = [0]*n
pri = [1]*n
for i in range(n):
    arr[i] = tuple(map(int, input().split()))

for i in range(n):
    v1 = arr[i]
    for v2 in arr:
        pri[i] += int(v1[0] < v2[0] and v1[1] < v2[1])
    
print(' '.join(map(str, pri)))
