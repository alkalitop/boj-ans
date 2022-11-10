z = map(int, input().split())
nsum = 0
for i in z:
    nsum += i**2
print(nsum % 10)
