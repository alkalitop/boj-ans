A,B=map(int,input().split(' '))
C=int(input())
b=B+C
print((A+(b//60))%24,b%60)
