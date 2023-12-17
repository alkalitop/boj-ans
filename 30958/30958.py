input()

s = [0]*123

for t in list(input()):
    if 97 <= ord(t) <= 122: s[ord(t)] += 1

print(max(*s))
