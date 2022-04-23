class matrix:
    def __init__(self, data):
        self.raw = data
    
    @property
    def rlen(self):
        return len(self.raw)

    @property
    def clen(self):
        return len(self.raw[0])
    
    def mul(self, mat, p=0):
        data = [None]*self.rlen
        for i in range(self.rlen):
            tmp = [0]*mat.clen
            for j in range(mat.clen):
                for k in range(self.clen):
                    tmp[j] += self.raw[i][k]*mat.raw[k][j]
                if p: tmp[j] %= p
            data[i] = tmp
        self.raw = data
        return self

    def pow (self, n, p=0):
        if n == 1: return self
        t = self.pow(n//2, p)
        res = None
        if n % 2 == 1:
            res = t.mul(t, p).mul(self, p)
        else:
            res = t.mul(t, p)
        return res
