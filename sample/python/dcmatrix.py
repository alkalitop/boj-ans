# ©️ 2022 sanha1229

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
