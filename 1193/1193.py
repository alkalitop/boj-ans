n = int(input())
S = lambda x: x*(x+1)/2
k = 1
while S(k) < n:
    k += 1
L = int(S(k-1))
print('%d/%d'%(1+(n-L-1), k-(n-L-1)) if k % 2 == 0 else '%d/%d'%(k-(n-L-1), 1+(n-L-1)))
