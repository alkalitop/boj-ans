H,M=map(int,input().split(' '))
m=M+15
h=H+23+(m//60)
print(h%24,m%60)
