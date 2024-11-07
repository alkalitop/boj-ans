import copy

class matrix:
    def __init__(self, data):
        self.raw = copy.deepcopy(data)

    @property
    def rlen(self):
        return len(self.raw)

    @property
    def clen(self):
        return len(self.raw[0])

    def __getitem__(self, index):
        return self.raw[index]

    def copy(self):
        return matrix(self.raw)

    def add(self, mat, m=0):
        data = [None] * self.rlen
        for i in range(self.rlen):
            tmp = [0] * self.clen
            for j in range(self.clen):
                tmp[j] += self[i][j] + mat[i][j]
                if m: tmp[j] %= m
            data[i] = tmp
        return matrix(data)

    def __add__(self, arg):
        if isinstance(arg, matrix):
            return self.add(arg)
        elif isinstance(arg, tuple):
            return self.add(arg[0], arg[1])
        else:
            raise TypeError()

    def sub(self, mat, m=0):
        data = [None] * self.rlen
        for i in range(self.rlen):
            tmp = [0] * self.clen
            for j in range(self.clen):
                tmp[j] += self[i][j] - mat[i][j]
                if m: tmp[j] %= m
            data[i] = tmp
        return matrix(data)

    def __sub__(self, arg):
        if isinstance(arg, matrix):
            return self.sub(arg)
        elif isinstance(arg, tuple):
            return self.sub(arg[0], arg[1])
        else:
            raise ValueError()

    def mul_scala(self, sca, m=0):
        data = copy.deepcopy(self.raw)
        for i in range(self.rlen):
            for j in range(self.clen):
                if m:
                    data[i][j] = (data[i][j] % m) * (sca % m)
                    data[i][j] %= m
                else:
                    data[i][j] *= sca
        return matrix(data)

    def mul_matrix(self, mat, m=0):
        data = [None] * self.rlen
        for i in range(self.rlen):
            tmp = [0] * mat.clen
            for j in range(mat.clen):
                for k in range(self.clen):
                    tmp[j] += self[i][k] * mat[k][j]
                if m: tmp[j] %= m
            data[i] = tmp
        return matrix(data)

    def __mul__(self, arg):
        if isinstance(arg, int):
            return self.mul_scala(arg)
        elif isinstance(arg, matrix):
            return self.mul_matrix(arg)
        elif isinstance(arg, tuple):
            if isinstance(arg[0], int):
                return self.mul_scala(arg[0], arg[1])
            elif isinstance(arg[0], matrix):
                return self.mul_matrix(arg[0], arg[1])
            else:
                raise ValueError()
        else:
            raise ValueError()

    def __rmul__(self, arg):
        if isinstance(arg, int):
            return self.mul_scala(arg)
        elif isinstance(arg, matrix):
            return self.mul_matrix(arg)
        elif isinstance(arg, tuple):
            if isinstance(arg[0], matrix):
                return self.mul_matrix(arg[0], arg[1])
            else:
                raise ValueError()
        else:
            raise ValueError()

    def mod(self, sca):
        data = copy.deepcopy(self.raw)
        for i in range(self.rlen):
            for j in range(self.clen):
                data[i][j] %= sca
        return matrix(data)

    def __mod__(self, arg):
        if isinstance(arg, int):
            return self.mod(arg)
        else:
            raise ValueError()

    def pow(self, n, m=0):
        if n == 0:
            return matrix.ones(self.rlen, self.clen)
        if n == 1:
            return self.copy()
        tmp = matrix(self.pow(n >> 1, m).raw)
        res = None
        if n & 1:
            res = tmp * (tmp, m) * (self.copy(), m)
        else:
            res = tmp * (tmp, m)
        return res

    def __pow__(self, arg):
        if isinstance(arg, int):
            return self.pow(arg)
        elif isinstance(arg, tuple):
            return self.pow(*arg)
        else:
            raise ValueError

    def transpose(self):
        data = [None] * self.clen
        for i in range(self.clen):
            data[i] = [0] * self.rlen
            for j in range(self.rlen):
                data[i][j] = self[j][i]
        return matrix(data)

    @staticmethod
    def rowvec(data):
        return matrix([data])

    @staticmethod
    def colvec(data):
        return matrix([data]).transpose()

    @staticmethod
    def zeros(r, c=1):
        return matrix([[0]*c for _ in range(r)])

    @staticmethod
    def ones(r, c=1):
        return matrix([[1]*c for _ in range(r)])

m = 31991
d, t = map(int, input().split())
a = matrix([[1 if i == 0 or (i > 0 and j == i-1) else 0 for j in range(d)] for i in range(d)])
v = matrix.zeros(d)
v[0][0] = 1
print((a**(t, m)*(v, m))[0][0])
