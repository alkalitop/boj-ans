import sys
input = sys.stdin.readline

N = int(input())
arr = [0]*N
for i in range(0, N):
    arr[i] = tuple(map(int, input().split()))
arr.sort()
for i in range(0, N):
    print(arr[i][0], arr[i][1])
