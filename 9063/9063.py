import sys
input = sys.stdin.readline

n = int(input())
x = [0]*n
y = [0]*n

for i in range(n):
    x[i], y[i] = map(int, input().split())
    
print((max(x)-min(x))*(max(y)-min(y)))
