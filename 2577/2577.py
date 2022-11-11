import sys
input = sys.stdin.readline 
a, b, c = map(int, [input() for i in range(3)])
count = [0]*10
prod = str(a*b*c)
for i in range(len(prod)):
    count[int(prod[i])] = count[int(prod[i])] + 1
for i in range(10):
    print(count[i])
