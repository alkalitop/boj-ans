a, b = input().split()
la, lb = (len(a), len(b))

s = 0

for i in range(la): s += int(a[i])*2**(la-i-1)
for i in range(lb): s += int(b[i])*2**(lb-i-1)
   
print(bin(s)[2:])
