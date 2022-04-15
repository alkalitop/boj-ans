import sys
input = sys.stdin.readline

mapping = list('0abcdefghijklmnopqrstuvwxyz')
L = int(input())
S = input()

H = 0
for i in range(L):
    H += mapping.index(S[i])*(31**i)

print(H % 1234567891)
