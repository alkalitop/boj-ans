import sys
input = sys.stdin.readline

D = [0]*21
D[1]=0
D[2]=1

for i in range(3, 21):
    D[i] = (i-1)*(D[i-1]+D[i-2])

for _ in range(int(input())):
    print(D[int(input())])
