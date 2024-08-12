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
                        
n, f1, f2, f3, c = map(int, input().split())
m = 10**9+7

h = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]

t0 = [[14], [6], [2], [8], [2]]
t1 = [[2], [1], [1]]
t2 = [[3], [2], [1]]
t3 = [[4], [2], [1]]

if n <= 6:
    p0 = t0[:3][3-n][0]
    p1 = t1[3-n][0]
    p2 = t2[3-n][0]
    p3 = t3[3-n][0]
else:
    p0 = matrix([
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1]
    ]).pow(n-6, m-1).mul(matrix(t0), m-1).raw[0][0]
    p1 = matrix(h).pow(n-6, m-1).mul(matrix(t1), m-1).raw[0][0]
    p2 = matrix(h).pow(n-6, m-1).mul(matrix(t2), m-1).raw[0][0]
    p3 = matrix(h).pow(n-6, m-1).mul(matrix(t3), m-1).raw[0][0]

print(pow(c, p0, m)*pow(f1, p1, m)*pow(f2, p2, m)*pow(f3, p3, m)%m)
