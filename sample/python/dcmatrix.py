class matrix:
    def __init__(self, data):
        self.raw = data
        self.__rlen = len(data)
        self.__clen = len(data[0])
    
    @property
    def rlen(self):
        return self.__rlen

    @property
    def clen(self):
        return self.__clen
    
    def mul(self, mat):
        data = [None]*self.rlen
        for i in range(self.rlen):
            tmp = [0]*mat.clen
            for j in range(mat.clen):
                #tmp = [0]*mat.clen
                for k in range(self.clen):
                    tmp[j] += self.raw[i][k]*mat.raw[k][j]
            data[i] = tmp
        self.raw = data
        self.__rlen = len(data)
        self.__clen = len(data[0])
