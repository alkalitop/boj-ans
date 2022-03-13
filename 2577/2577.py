import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
prod = str(a*b*c)
for i in range(0, len(prod)):
    count[int(prod[i])] = count[int(prod[i])] + 1
for i in range(0, 10):
    print(count[i])
