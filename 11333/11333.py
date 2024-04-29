d = 10**9+7

s = [0]*10001
s[0] = 1
s[3] = 3

for i in range(6, 10001, 3):
    s[i] = 3*s[i-3]
    s[i] %= d
    for j in range(i-6, -1, -3):
        s[i] += 2*((i-j)//3)*s[j]
        s[i] %= d

for i in range(int(input())):
    print(s[int(input())])
