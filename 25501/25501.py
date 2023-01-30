def sol (s):
    l, r = (0, len(s)-1)
    cnt = 0
    while 1:
        cnt += 1
        if l >= r or s[l] != s[r]: break
        l += 1
        r -= 1
    return cnt

for i in range(int(input())):
    p = input()
    print(1 if p == p[::-1] else 0, sol(p))
