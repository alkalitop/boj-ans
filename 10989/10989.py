import sys
input = sys.stdin.readline

n = int(input())
data = [0]*10000

for _ in range(n):
    k = int(input())-1
    data[k] += 1
    
for k in range(10000):
    if data[k] > 0:
        for _ in range(data[k]): print(k+1)
