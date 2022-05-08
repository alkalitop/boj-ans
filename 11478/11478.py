A = set()
s = input()

for i in range(len(s)+1):
    for j in range(i+1, len(s)+1):
        A.add(s[i:j])

print(len(A))
