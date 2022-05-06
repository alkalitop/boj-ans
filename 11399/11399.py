import sys
input = sys.stdin.readline

n = int(input())
p = sorted(list(map(int, input().split())))

acc = 0
size = len(p)
for i in range(0, size):
    acc += (size-i)*p[i]
    
print(acc)
