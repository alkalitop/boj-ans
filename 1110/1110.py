N = int(input())
f = lambda x: (x%10)*10 + (((x//10)+(x%10))%10)
gen = f(N)
cyc = 1
while gen != N:
	gen = f(gen)
	cyc = cyc + 1
print(cyc)
