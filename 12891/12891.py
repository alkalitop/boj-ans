len_s, len_p = map(int, input().split())
s = input()
min_a, min_c, min_g, min_t = map(int, input().split())

amt = {
    'A': 0,
    'C': 0,
    'G': 0,
    'T': 0
}

check = lambda: amt['A'] >= min_a and amt['C'] >= min_c and amt['G'] >= min_g and amt['T'] >= min_t

cnt = 0
for i in range(len_p):
    amt[s[i]] += 1

for i in range(len_s - len_p + 1):
    if check(): cnt += 1
    amt[s[i]] -= 1
    if i < len_s - len_p: amt[s[i+len_p]] += 1

print(cnt)
