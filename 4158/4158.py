import sys
input = sys.stdin.readline

n, m = map(int, input().split())

while n != 0 and m != 0:
    A = [0]*m
    B = [0]*n

    for i in range(n):
        A[i] = int(input())
    
    for i in range(m):
        B[i] = int(input())

    print(len(set(A) & set(B)))

    n, m = map(int, input().split())
    
    
