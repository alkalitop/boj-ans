a,b,c=map(int,input().split(' '))
M=lambda x,y,z: x>=y and x>=z
if (a-b)*(b-c)*(c-a)!=0:
    print(100*(a if M(a,b,c) else (b if M(b,c,a) else c)))
else:
    t=2*((a==b)+(b==c)+(c==a))-3*(a==b==c)
    print(10**(1+t)+(a if a==b or a==c else b)*10**t)
