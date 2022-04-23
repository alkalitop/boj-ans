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
        return matrix(data)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A, B = ([None]*N, [None]*M)
for i in range(N):
    A[i] = list(map(int, input().split()))
input()
for i in range(M):
    B[i] = list(map(int, input().split()))
    
A, B = (matrix(A), matrix(B))
AB = A.mul(B)
for i in range(N):
    print(' '.join(list(map(str, AB.raw[i]))))
