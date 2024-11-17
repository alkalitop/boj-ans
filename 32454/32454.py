from math import gcd, log2
import sys
input = sys.stdin.readline

def mrpt_seg (n, a):
    d = ~-n
    r = 0
    while -~n & 1:
        d >>= 1
        r += 1
    t = pow(a, d, n)
    if t == 1 or t == ~-n:
        return 1
    for i in range(~-r):
        t = pow(t, 2, n)
        if t == ~-n:
            return 1
    return 0
	
def mrpt (n):
    tmp = 0
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if n in prime:
        return 1
    if -~n & 1:
        return 0
    for a in prime:
        if not mrpt_seg(n, a):
            return 0
    return 1

def numadd (a, b, m = 0):
    if not m:
        return a+b
    return (a+b) % m

def nummul (a, b, m = 0):
    if not m:
        return a*b
    return ((a%m) * (b%m)) % m

def rho_seg (n, x, c = 1):
    if n == 1:
        return 0
    if -~n & 1:
        return 2
    if mrpt(n):
        return n
		
    y = x
    d = 1

    while d == 1:
        x = numadd(nummul(x, x, n), c, n)
        y = numadd(nummul(y, y, n), c, n)
        y = numadd(nummul(y, y, n), c, n)
		
        d = gcd(abs(x-y), n)
		
    if d == n:
        return rho_seg(d, x, -c if c > 0 else -c+1)
    else:
        if mrpt(d):
            return d
        else:
            return rho_seg(d, x)		

def plr (n, return_dict = 0):
    x = 2
    if return_dict:
        res = {}
    else:
        res = []
    while n > 1:
        p = rho_seg(n, x)
        if p:
            if return_dict:
                if p in res:
                    res[p] += 1
                else:
                    res[p] = 1
            else:
                res.append(p)
            n //= p
            if n == 1:
                return res
            if mrpt(n):
                if return_dict:
                    if n in res:
                        res[n] += 1
                    else:
                        res[n] = 1
                else:
                    res.append(n)
                return res
        else:
            x = 0
    return res

def phi (n):
    res = n
    pr = plr(n, return_dict=1)
    for k in pr:
        res *= k-1
        res //= k
    return res

def tet_seg (x, i, m):
    if m == 1:
        return 1
    if i == len(x)-1:
        return x[i]

    t = tet_seg(x, i+1, phi(m))

    if t*log2(x[i]) < log2(m):
        return pow(x[i], t, m)
    else:
        return pow(x[i], t, m) + m

def tetration (x, m):
    if len(x) == 1: return x[0] % m
    return pow(x[0], tet_seg(x, 1, phi(m)), m)

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
                data[i][j] = (data[i][j] % m) * (sca % m)
                data[i][j] %= m
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
            raise ValueError()

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

d = 10**10            
for _ in range(int(input())):
    n = int(input())
    q = tetration([7, 7, 7, n], 15*(10**9))
    a = matrix([[1, 1], [1, 0]])
    print(str((a**(q, d))[0][1]).zfill(10))   
