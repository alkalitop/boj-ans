z = list(map(int, input().split()))
nsum = 0
for i in range(0, 5):
    nsum += z[i]**2
print(nsum % 10)
