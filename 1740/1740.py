n = int(input())

i = 0
s = 0

for b in bin(n)[2:][::-1]:
    s += int(b)*(3**i)
    i += 1
    
print(s)
