import sys
input = sys.stdin.readline

mod = 10**9+7

class vector:
    def __init__(self, size=0, default=0):
        if type(size) == list:
            self.raw = size
        else:
            self.raw = [default]*size

    def __getitem__(self, index):
        if index < self.size():
            return self.raw[index]
        else:
            raise IndexError

    def __setitem__(self, index, value):
        if index < self.size():
            self.raw[index] = value
        else:
            raise IndexError

    def size(self):
        return len(self.raw)

    def empty(self):
        return self.size() == 0

    def resize(self, size, default=0):
        if self.size() >= size:
            self.raw = self.raw[:size]
        else:
            while self.size() < size:
                self.raw.append(default)

    def push_back(self, value):
        self.raw.append(value)

def ipow(x, p):
    ret = 1
    piv = x
    while p:
        if p & 1: 
            ret = ret * piv % mod
        piv = piv * piv % mod
        p >>= 1
    return ret

def berlekamp_massey(x):
    ls, cur = vector(), vector()
    lf, ld = 0, 0
    for i in range(x.size()):
        t = 0
        for j in range(cur.size()):
            t = (t + x[i-j-1] * cur[j]) % mod
        if (t - x[i]) % mod == 0: continue
        if cur.empty():
            cur.resize(i+1)
            lf = i
            ld = (t - x[i]) % mod
            continue
        k = -(x[i] - t) * ipow(ld, mod - 2) % mod
        c = vector(i-lf-1)
        c.push_back(k)
        for j in ls: c.push_back(-j * k % mod)
        if c.size() < cur.size(): c.resize(cur.size())
        for j in range(cur.size()):
            c[j] = (c[j] + cur[j]) % mod
        if i-lf+ls.size() >= cur.size():
            ls, lf, ld = cur, i, (t - x[i]) % mod
        cur = c
    for i in range(cur.size()):
        cur[i] = (cur[i] % mod + mod) % mod
    return cur

def get_nth(rec, dp, n):
    m = rec.size()
    s, t = vector(m), vector(m)
    s[0] = 1
    if m != 1: t[1] = 1
    else: t[0] = rec[0]
    def mul(v, w):
        m = v.size()
        t = vector(2*m)
        for j in range(m):
            for k in range(m):
                t[j+k] += v[j] * w[k] % mod
                if t[j+k] >= mod: t[j+k] -= mod
        for j in range(2*m-1, m-1, -1):
            for k in range(1, m+1):
                t[j-k] += t[j] * rec[k-1] % mod
                if t[j-k] >= mod: t[j-k] -= mod
        t.resize(m)
        return t
    while n:
        if n & 1:
            s = mul(s, t)
        t = mul(t, t)
        n //= 2

    ret = 0
    for i in range(m):
        ret += s[i] * dp[i] % mod
    return ret % mod

def guess_nth_term(x, n):
    if n < x.size(): return x[n] % mod
    v = berlekamp_massey(x)
    if v.empty(): return 0
    return get_nth(v, x, n)

seq = vector([0,1,2,6,16,36,80,178,394,870,1920,4236,9344,
 20610,45458,100262,221136,487732,1075728,2372594,
 5232922,11541574,25455744,56144412,123830400,
 273116546,602377506,1328585414,2930287376,
 6462952260,14254489936,31439267250,69341486762])

while 1:
    n = input()
    if not len(n): break
    print(guess_nth_term(seq, int(n)))



