import sys
input = sys.stdin.readline

N = int(input())
arr = [0]*N
for i in range(0, N):
    x, y = map(int, input().split())
    arr[i] = (y, x)
arr.sort()
for i in range(0, N):
    print(arr[i][1], arr[i][0])
