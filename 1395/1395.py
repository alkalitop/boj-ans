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

class SumSegmentTree:

    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)<<2
        self.tree = [0]*(self.size)
        self.lazy = [0]*(self.size)
        self.merge = lambda a,b: a+b
        segmentify(tree=self.tree, index=(0, len(self.arr)-1, 1), merge=self.merge, arr=self.arr)

    def propagate(self, index):
        start, end, idx = index
        if self.lazy[idx] != 0:
            self.tree[idx] = abs((end - start + 1) - self.tree[idx]) if self.lazy[idx] & 1 else self.tree[idx]
            if start != end:
                self.lazy[lc(idx)] += self.lazy[idx]
                self.lazy[rc(idx)] += self.lazy[idx]
            self.lazy[idx] = 0
    
    def sum(self, L, R, index=0):
        if not index: index = (0, len(self.arr)-1 ,1)
        start, end, idx = index

        self.propagate(index)
    
        if R < start or L > end:
            return 0
        elif L <= start and R >= end:
            return self.tree[idx]
        else:
            mid = (start+end)//2
            a = self.sum(L, R, (start, mid, lc(idx)))
            b = self.sum(L, R, (mid+1, end, rc(idx)))
            return self.merge(a, b)
        
    def ap_not(self, L, R, index=0):
        if not index: index = (0, len(self.arr)-1, 1)
        start, end, idx = index

        self.propagate(index)
    
        if R < start or L > end:
            return
        elif L <= start and R >= end:
            self.tree[idx] = abs((end - start + 1) - self.tree[idx])
            if start != end:
                self.lazy[lc(idx)] += 1
                self.lazy[rc(idx)] += 1
            return
    
        mid = (start+end)//2
        self.ap_not(L, R, (start, mid, lc(idx)))
        self.ap_not(L, R, (mid+1, end, rc(idx)))
        self.tree[idx] = self.merge(self.tree[lc(idx)], self.tree[rc(idx)])
        
n, m = map(int, input().split())
s = SumSegmentTree([0]*n)

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        s.ap_not(b-1, c-1)
    else:
        print(s.sum(b-1, c-1))
