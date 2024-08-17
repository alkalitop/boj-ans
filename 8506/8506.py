from math import comb

class matrix:
    def __init__(self, data):
        self.raw = data
    
    @property
    def rlen(self):
        return len(self.raw)

    @property
    def clen(self):
        return len(self.raw[0])
    
    def add(self, mat, p=0):
        data = [None]*self.rlen
        for i in range(self.rlen):
            tmp = [0]*self.clen
            for j in range(self.clen):
                tmp[j] += self.raw[i][j]+mat.raw[i][j]
                if p: tmp[j] %= p
            data[i] = tmp
        return matrix(data)

    def sub(self, mat, p=0):
        data = [None]*self.rlen
        for i in range(self.rlen):
            tmp = [0]*self.clen
            for j in range(self.clen):
                tmp[j] += self.raw[i][j]-mat.raw[i][j]
                if p: tmp[j] %= p
            data[i] = tmp
        return matrix(data)

    def mul(self, mat, p=0):
        data = [None]*self.rlen
        for i in range(self.rlen):
            tmp = [0]*mat.clen
            for j in range(mat.clen):
                for k in range(self.clen):
                    tmp[j] += self.raw[i][k]*mat.raw[k][j]
                if p: tmp[j] %= p
            data[i] = tmp
        return matrix(data)

    def pow(self, n, p=0):
        if n == 1: return matrix(self.raw)
        t = matrix(self.pow(n//2, p).raw)
        res = None
        if n % 2 == 1:
            res = t.mul(t, p).mul(matrix(self.raw), p)
        else:
            res = t.mul(t, p)
        return res

def msum(a, m):
    r = a[0] % m
    for i in range(1, len(a)):
        r += a[i] % m
        r %= m
    return r

def mprod(a, m):
    r = a[0] % m
    for i in range(1, len(a)):
        r *= a[i] % m
        r %= m
    return r

def f(n, m):
    return matrix([[1, 1], [1, 0]]).pow(n, m).raw[1][0] if n else 0

def fps(n, k):
    m = 10**9
    s = 1 if n & 1 else -1
    if k == 0:
        return n % m
    elif k == 1:
        return f(n+2, m) - 1
    elif k == 2:
        return mprod([f(n, m), f(n+1, m)], m)
    elif k == 3:
        d = 10
        t = [0]*3
        t[0] = f(3*n+2, m*d)
        t[1] = mprod([6, s, f(n-1, m*d)], m*d)
        t[2] = 5
        return (msum(t, m*d) // d) % m
    elif k == 4:
        d = 25
        t = [0]*4
        t[0] = f(4*n+2, m*d)
        t[1] = mprod([4, s, f(2*n+1, m*d)], m*d)
        t[2] = mprod([6, n], m*d)
        t[3] = 3
        return (msum(t, m*d) // d) % m
    elif k == 5:
        d = 550
        t = [0]*5
        t[0] = mprod([4, f(5*n+2, m*d)], m*d)
        t[1] = mprod([2, f(5*n+4, m*d)], m*d)
        t[2] = mprod([55, s, f(3*n+1, m*d)], m*d)
        t[3] = mprod([220, f(n+2, m*d)], m*d)
        t[4] = -175
        return (msum(t, m*d) // d) % m
    elif k == 6:
        d = 500
        t = [0]*5
        t[0] = f(6*n+2, m*d)
        t[1] = f(6*n+4, m*d)
        tmp = msum([f(4*n+1, m*d), f(4*n+3, m*d), 5], m*d)
        t[2] = mprod([8, s, tmp], m*d)
        t[3] = mprod([60, f(2*n, m*d)], m*d)
        t[4] = mprod([60, f(2*n+2, m*d)], m*d)
        return (msum(t, m*d) // d) % m
    elif k == 7:
        d = 79750
        t = [0]*5
        t[0] = mprod([22, f(7*n+2, m*d)], m*d)
        t[1] = mprod([88, f(7*n+4, m*d)], m*d)
        t21 = mprod([55, f(n-1, m*d)], m*d)
        t22 = f(5*n+1, m*d)
        t23 = mprod([2, f(5*n+3, m*d)], m*d)
        tmp = msum([t21, t22, t23], m*d)
        t[2] = mprod([406, s, tmp], m*d)
        t[3] = mprod([6699, f(3*n+2, m*d)], m*d)
        t[4] = 17375
        return (msum(t, m*d) // d) % m
    elif k == 8:
        d = 1875
        t = [0]*5
        t[0] = f(8*n+4, m*d)
        t11 = mprod([14, f(2*n+1, m*d)], m*d)
        t12 = f(6*n+3, m*d)
        tmp = msum([t11, t12], m*d)
        t[1] = mprod([12, s, tmp], m*d)
        t[2] = mprod([84, f(4*n+2, m*d)], m*d)
        t[3] = mprod([210, n], m*d)
        t[4] = 105
        return (msum(t, m*d) // d) % m
    elif k == 9:
        d = 7576250
        t = [0]*9
        t[0] = mprod([1276, f(9*n+4, m*d)], m*d)
        t[1] = mprod([319, f(9*n+5, m*d)], m*d)
        t[2] = mprod([18810, s, f(7*n+3, m*d)], m*d)
        t[3] = mprod([3762, s, f(7*n+4, m*d)], m*d)
        t[4] = mprod([119016, f(5*n+2, m*d)], m*d)
        t[5] = mprod([39672, f(5*n+3, m*d)], m*d)
        t[6] = mprod([509124, s, f(3*n+1, m*d)], m*d)
        t[7] = mprod([1527372, f(n+2, m*d)], m*d)
        t[8] = -1173125
        return (msum(t, m*d) // d) % m
    elif k == 10:
        d = 962500
        t = [0]*11
        t[0] = mprod([36960, s, f(4*n+3, m*d)], m*d)
        t[1] = mprod([12320, -s, f(4*n+4, m*d)], m*d)
        t[2] = mprod([3080, s, f(8*n+7, m*d)], m*d)
        t[3] = mprod([1760, -s, f(8*n+8, m*d)], m*d)
        t[4] = mprod([38808, s], m*d)
        t[5] = mprod([-64680, f(2*n+1, m*d)], m*d)
        t[6] = mprod([129360, f(2*n+2, m*d)], m*d)
        t[7] = mprod([-13860, f(6*n+5, m*d)], m*d)
        t[8] = mprod([10395, f(6*n+6, m*d)], m*d)
        t[9] = mprod([-308, f(10*n+9, m*d)], m*d)
        t[10] = mprod([196, f(10*n+10, m*d)], m*d)
        return (msum(t, m*d) // d) % m
        # (-36960*(-1)**n*F(4*n + 3) + 12320*(-1)**n*F(4*n + 4) - 3080*(-1)**n*F(8*n + 7) + 1760*(-1)**n*F(8*n + 8) - 38808*(-1)**n - 64680*F(2*n + 1) + 129360*F(2*n + 2) - 13860*F(6*n + 5) + 10395*F(6*n + 6) - 308*F(10*n + 9) + 196*F(10*n + 10))
    elif k == 11:
        d = 685306250
        t = [0]*11
        t[0] = mprod([101315676, s, f(n-1, m*d)], m*d)
        t[1] = mprod([16447350, -s, f(5*n+4, m*d)], m*d)
        t[2] = mprod([13157880, s, f(5*n+5, m*d)], m*d)
        t[3] = mprod([1079177, -s, f(9*n+8, m*d)], m*d)
        t[4] = mprod([698291, s, f(9*n+9, m*d)], m*d)
        t[5] = mprod([36184170, f(3*n+2, m*d)], m*d)
        t[6] = mprod([5406830, f(7*n+6, m*d)], m*d)
        t[7] = mprod([-2911370, f(7*n+7, m*d)], m*d)
        t[8] = mprod([98078, f(11*n+10, m*d)], m*d)
        t[9] = mprod([-59508, f(11*n+11, m*d)], m*d)
        t[10] = 77153125
        return (msum(t, m*d) // d) % m
        #(101315676*(-1)**n*F(n) - 101315676*(-1)**n*F(n + 1) + 16447350*(-1)**n*F(5*n + 4)
        # - 13157880*(-1)**n*F(5*n + 5) + 1079177*(-1)**n*F(9*n + 8) - 698291*(-1)**n*F(9*n + 9)
        # + 36184170*F(3*n + 2) + 5406830*F(7*n + 6) - 2911370*F(7*n + 7) + 98078*F(11*n + 10) - 59508*F(11*n + 11)
        # + 77153125)/685306250
    elif k == 12:
        d = 625000
        t = [0]*12
        t[0] = mprod([31680, s, f(2*n+1, m*d)], m*d)
        t[1] = mprod([8800, s, f(6*n+5, m*d)], m*d)
        t[2] = mprod([4400, -s, f(6*n+6, m*d)], m*d)
        t[3] = mprod([480, s, f(10*n+9, m*d)], m*d)
        t[4] = mprod([288, -s, f(10*n+10, m*d)], m*d)
        t[5] = mprod([36960, n], m*d)
        t[6] = mprod([19800, f(4*n+2, m*d)], m*d)
        t[7] = mprod([-2640, f(8*n+7, m*d)], m*d)
        t[8] = mprod([1760, f(8*n+8, m*d)], m*d)
        t[9] = mprod([-40, f(12*n+11, m*d)], m*d)
        t[10] = mprod([25, f(12*n+12, m*d)], m*d)
        t[11] = 18480
        return (msum(t, m*d) // d) % m
        # (-31680*(-1)**n*F(2*n + 1) - 8800*(-1)**n*F(6*n + 5) + 4400*(-1)**n*F(6*n + 6) - 480*(-1)**n*F(10*n + 9)
        # + 288*(-1)**n*F(10*n + 10) + 36960*n - 19800*F(4*n + 3) + 19800*F(4*n + 4) - 2640*F(8*n + 7)
        # + 1760*F(8*n + 8) - 40*F(12*n + 11) + 25*F(12*n + 12) + 18480)/625000
    elif k == 13:
        d = 1785222781250
        t = [0]*13
        t[0] = mprod([73522615023, s, f(3*n+1, m*d)], m*d)
        t[1] = mprod([14648183836, -s, f(7*n+6, m*d)], m*d)
        t[2] = mprod([10141050348, s, f(7*n+7, m*d)], m*d)
        t[3] = mprod([664282294, -s, f(11*n+10, m*d)], m*d)
        t[4] = mprod([417975376, s, f(11*n+11, m*d)], m*d)
        t[5] = mprod([196060306728, f(n+2, m*d)], m*d)
        t[6] = mprod([37132633850, f(5*n+4, m*d)], m*d)
        t[7] = mprod([-14853053540, f(5*n+5, m*d)], m*d)
        t[8] = mprod([3986872266, f(9*n+8, m*d)], m*d)
        t[9] = mprod([-2345218980, f(9*n+9, m*d)], m*d)
        t[10] = mprod([51096434, f(13*n+12, m*d)], m*d)
        t[11] = mprod([-31359614, f(13*n+13, m*d)], m*d)
        t[12] = -148395828125
        return (msum(t, m*d) // d) % m
        # (73522615023*(-1)**n*F(3*n + 2) - 73522615023*(-1)**n*F(3*n + 3) + 14648183836*(-1)**n*F(7*n + 6)
        # - 10141050348*(-1)**n*F(7*n + 7) + 664282294*(-1)**n*F(11*n + 10) - 417975376*(-1)**n*F(11*n + 11)
        # + 196060306728*F(n) + 196060306728*F(n + 1) + 37132633850*F(5*n + 4) - 14853053540*F(5*n + 5)
        # + 3986872266*F(9*n + 8) - 2345218980*F(9*n + 9) + 51096434*F(13*n + 12) - 31359614*F(13*n + 13)
        # - 148395828125)/1785222781250

def lps(n, k):
    m = 10**9
    r = 0
    for i in range(k+1):
        r += mprod([comb(k, i), pow(2, i, m), (-1 if (k-i) & 1 else 1), fps(n+1, i)], m)
        r %= m
    return r

print(str(lps(*map(int, input().split()))).zfill(9))
