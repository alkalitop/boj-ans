mod = 10**9+7

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

n, m = map(int, input().split())

if m == 1:
    print(pow(2, n, mod))
elif m == 2:
    s = matrix([
        [14],
        [4]
    ])
    t = matrix([
        [3, 2],
        [1, 0]
    ])
    if n <= 2:
        print(s.raw[-n][0])
    else:
        print((t.pow(n-2, mod).mul(s, mod)).raw[0][0])
elif m == 3:
    s = matrix([
        [322],
        [50],
        [8]
    ])
    t = matrix([
        [6, 3, -2],
        [1, 0, 0],
        [0, 1, 0]
    ])
    if n <= 3:
        print(s.raw[-n][0])
    else:
        print((t.pow(n-3, mod).mul(s, mod)).raw[0][0])
elif m == 4:
    s = matrix([
        [275690],
        [23858],
        [2066],
        [178],
        [16]
    ])
    t = matrix([
        [10, 20, -21, -30, 8],
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0]
    ])
    if n <= 5:
        print(s.raw[-n][0])
    else:
        print((t.pow(n-5, mod).mul(s, mod)).raw[0][0])
elif m == 5:
    s = matrix([
        [33293940],
        [630302833],
        [481942340],
        [119310334],
        [5735478],
        [275690],
        [13262],
        [634],
        [32]
    ])
    t = matrix([
        [21, 9, -278, 73, 790, -662, 29, 69, -10],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0]
    ])
    if n <= 9:
        print(s.raw[-n][0])
    else:
        print((t.pow(n-9, mod).mul(s, mod)).raw[0][0])
