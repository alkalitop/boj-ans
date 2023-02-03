m = 10**9
D = [0]*(10**6+1)
D[1]=0
D[2]=1

n = int(input())
for i in range(3, n+1):
    D[i] = (i-1)*(D[i-1]+D[i-2]) % m
	
print(D[n])
