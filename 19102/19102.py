from math import isqrt

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
    if n < x.size(): return x[n]
    v = berlekamp_massey(x)
    if v.empty(): return 0
    return get_nth(v, x, n)

size = 199

h = [0]*(size + 1)
h[0] = 2
h[1] = 3
h[2] = 6


for i in range(3, size+1):
    h[i] = 4*h[i-1] + 17*h[i-2] - 12*h[i-3] - 16

b = [0]*size

for i in range(1, size):
    b[i] = (3*h[i+1]*h[i] + 9*h[i+1]*h[i-1] + 9*(h[i]**2) + 27*h[i]*h[i-1] - 18*h[i+1] - 126*h[i] - 81*h[i-1] - 192)
    

a = [0]*size

for i in range(1, size):
    a[i] = b[i] + 4**i

c = [0]*size

for i in range(2, size):
    c[i] = int(isqrt(a[i])) % mod

for _ in range(int(input())):
    print(guess_nth_term(vector(c), int(input())))
