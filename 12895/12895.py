import sys
input = sys.stdin.readline

def lc(idx):
    return idx << 1

def rc(idx):
    return (idx << 1) + 1

def segmentify(tree, index, merge, arr):
    start, end, idx = index
    
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    
    mid = (start+end)//2
    a = segmentify(tree, (start, mid, lc(idx)), merge, arr)
    b = segmentify(tree, (mid+1, end, rc(idx)), merge, arr)
    tree[idx] = merge(a, b)
    return tree[idx]

class ORSegmentTree:

    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)<<2
        self.tree = [0]*(self.size)
        self.lazy = [0]*(self.size)
        self.merge = lambda a,b: a|b
        segmentify(tree=self.tree, index=(0, len(self.arr)-1, 1), merge=self.merge, arr=self.arr)

    def propagate(self, index):
        start, end, idx = index
        if self.lazy[idx] != 0:
            self.tree[idx] = self.lazy[idx]
            if start != end:
                self.lazy[lc(idx)] = self.lazy[idx]
                self.lazy[rc(idx)] = self.lazy[idx]
            self.lazy[idx] = 0
    
    def inv_or(self, L, R, index=0):
        if not index: index = (0, len(self.arr)-1 ,1)
        start, end, idx = index

        self.propagate(index)
    
        if R < start or L > end:
            return 0
        elif L <= start and R >= end:
            return self.tree[idx]
        else:
            mid = (start+end)//2
            a = self.inv_or(L, R, (start, mid, lc(idx)))
            b = self.inv_or(L, R, (mid+1, end, rc(idx)))
            return self.merge(a, b)
        
    def replace(self, L, R, value, index=0):
        if not index: index = (0, len(self.arr)-1, 1)
        start, end, idx = index

        self.propagate(index)
    
        if R < start or L > end:
            return
        elif L <= start and R >= end:
            self.lazy[idx] = value
            self.propagate(index)
            return
    
        mid = (start+end)//2
        self.replace(L, R, value, (start, mid, lc(idx)))
        self.replace(L, R, value, (mid+1, end, rc(idx)))
        self.tree[idx] = self.merge(self.tree[lc(idx)], self.tree[rc(idx)])

n, t, q = map(int, input().split())
s = ORSegmentTree([1]*n)
for _ in range(q):
    c = input()
    if c[0] == 'C':
        x, y, z = map(int, c[2:].split())
        if x > y: x, y = y, x
        s.replace(x-1, y-1, 1 << (z-1))
    else:
        x, y = map(int, c[2:].split())
        if x > y: x, y = y, x
        print(sum(map(int, list(bin(s.inv_or(x-1, y-1))[2:]))))
