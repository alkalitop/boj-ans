d = 10**9+7

def segmentify(tree, index, merge, arr):
    start, end, idx = index
    
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    
    mid = (start+end)//2
    a = segmentify(tree, (start, mid, idx<<1), merge, arr)
    b = segmentify(tree, (mid+1, end, (idx<<1)+1), merge, arr)
    tree[idx] = merge(a, b)
    return tree[idx]

def pow (a, n):
    if n == 0:
        return 1
    t = pow(a, n//2)
    if n % 2 == 1:
        return t*t*a % d
    else:
        return t*t % d

def nz(t):
    return (abs(t) or 1)%d

def sg(x, y):
    if x>0 and y>0:
        return 1
    else:
        return -1

class ProdSegmentTree:

    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)<<2
        self.tree = [1]*(self.size)    
        self.merge = lambda a,b: (nz(a)*nz(b))%d
        segmentify(tree=self.tree, index=(0,(self.size>>2)-1,1), merge=self.merge, arr=self.arr)
    
    def prod(self, L, R, index=0):
        if not index: index = (0,(self.size>>2)-1,1)
        start, end, idx = index # 리스트 시작 인덱스, 리스트 끝 인덱스, 트리 인덱스
    
        if R < start or L > end:
            return 1
        elif L <= start and R >= end:
            c = self.tree[idx]
            return c if c > 0 else 0
        else:
            mid = (start+end)//2
            a = self.prod(L, R, (start, mid, idx<<1))
            b = self.prod(L, R, (mid+1, end, (idx<<1)+1))
            c = self.merge(a, b)
            return c if c > 0 else 0

    def mul(self, target, value, index=0):
        if not index: index = (0,(self.size>>2)-1,1)
        start, end, idx = index # 리스트 시작 인덱스, 리스트 끝 인덱스, 트리 인덱스
    
        if target < start or target > end: return
    
        self.tree[idx] = (nz(self.tree[idx])*nz(value))%d

        if start == end: 
            self.arr[target] *= value
            self.arr[target] %= d
            return
    
        mid = (start+end)//2
        self.mul(target, value, (start, mid, idx<<1))
        self.mul(target, value, (mid+1, end, (idx<<1)+1))        
                        
    def replace(self, target, v, index=0):
        u = self.arr[target]
        k = pow(u, d-2)
        
        self.mul(target, v)
        self.arr[target] = v
        self.mul(target, k)
        self.arr[target] = v

class SumSegmentTree:

    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)<<2
        self.tree = [0]*(self.size)
        self.merge = lambda a,b: a+b
        segmentify(tree=self.tree, index=(0,(self.size>>2)-1,1), merge=self.merge, arr=self.arr)
    
    def sum(self, L, R, index=0):
        if not index: index = (0,(self.size>>2)-1,1)
        start, end, idx = index # 리스트 시작 인덱스, 리스트 끝 인덱스, 트리 인덱스
    
        if R < start or L > end:
            return 0
        elif L <= start and R >= end:
            return self.tree[idx]
        else:
            mid = (start+end)//2
            a = self.sum(L, R, (start, mid, idx<<1))
            b = self.sum(L, R, (mid+1, end, (idx<<1)+1))
            return self.merge(a, b)
        
    def add(self, target, value, index=0):
        if not index: index = (0,(self.size>>2)-1,1)
        start, end, idx = index # 리스트 시작 인덱스, 리스트 끝 인덱스, 트리 인덱스
    
        if target < start or target > end: return
    
        self.tree[idx] += value
        if start == end: 
            self.arr[target] += value
            return
    
        mid = (start+end)//2
        self.add(target, value, (start, mid, idx<<1))
        self.add(target, value, (mid+1, end, (idx<<1)+1))
        
    def replace(self, target, value):
        self.add(target, value-self.arr[target])        
                        
        
n, m, k = map(int, input().split())
A = [0]*n
B = [0]*n

for i in range(n):
    x = int(input())
    A[i] = x
    B[i] = 0 if x > 0 else 1
    
    
S = ProdSegmentTree(A)
T = SumSegmentTree(B)
    
for i in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        S.replace(b-1, c)
        if T.arr[b-1] > 0 and c > 0:
            T.replace(b-1, 0)
        elif T.arr[b-1] == 0 and c == 0:
            T.replace(b-1, 1)
    else:
        if T.sum(b-1, c-1) > 0:
            print(0)
        else:
            print(S.prod(b-1, c-1))
        
    
