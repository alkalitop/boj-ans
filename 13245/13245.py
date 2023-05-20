I = input()

c = 0
n = len(I)
A = int(I)
a = list(map(int, list(I)))

for i in range(1, n+1):
    c += int(10**(n-i)) * ( (a[i-1]-1)*a[i-1]//2 )
    c += a[i-1] * (int(I[i:] if i < n else '0')+1)

for i in range(1, n+1):
    c += 45 * (n-i)*int(10**(n-i-1)) * a[i-1]
                     
print(c)
