s = (input(), input())
z = (len(s[0])+1, len(s[1])+1)

lcs = [['']*z[1] for _ in range(z[0])]

for i in range(1, z[0]):
    for j in range(1, z[1]):
        if s[0][i-1] == s[1][j-1]:
            lcs[i][j] = lcs[i-1][j-1] + s[0][i-1]
        else:
            p, q = lcs[i-1][j], lcs[i][j-1]
            lcs[i][j] = len(p)-len(q) > 0 and p or q

print(len(lcs[-1][-1]))
print(lcs[-1][-1])
