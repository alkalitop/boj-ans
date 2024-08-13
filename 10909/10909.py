from math import gcd
import sys
input = sys.stdin.readline

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


m, t = map(int, input().split())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    k = a**2 + b**2 + c**2 + d**2
    if gcd(m, k) != 1:
        print(0, 0, 0, 0)
    else:
        inv = matrix([
            [a, b, c, d],
            [-b, a, d, -c], 
            [-c, -d, a, b],
            [-d, c, -b, a]
        ])
        z = pow(k, m-2, m)
        print(*map(lambda x: x[0]*z%m, inv.mul(matrix([[1], [0], [0], [0]]), m).raw))

