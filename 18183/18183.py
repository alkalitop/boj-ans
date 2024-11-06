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

d = 998244353
n, m = map(int, input().split())

if n % 4 or m % 4:
    print(0)
else:
    n >>= 2
    m >>= 2
    if m == 1:
        print((2 * pow(3, n-1, d)) % d)
    elif m == 2:
        v = matrix.rowvec([2, 1])
        a = matrix([[18, 9], [16, 14]])
        k = 2 if n == 1 else pow(pow(2, n-2, d), d-2, d)
        print((k * v * (a**(n-1, d), d) * (matrix.ones(3), d))[0][0])
    elif m == 3:
        v = matrix.rowvec([4, 2, 0, 2, 1])
        a = matrix([
            [108, 54, 0, 54, 27],
            [96, 84, 0, 48, 42],
            [96, 48, 12, 48, 48],
            [96, 48, 0, 84, 42],
            [80, 64, 8, 64, 96]
        ])
        k = 4 if n == 1 else pow(pow(2, 2*n-3, d), d-2, d)
        print((k * v * (a**(n-1, d), d) * (matrix.ones(5), d))[0][0])
