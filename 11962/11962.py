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
            self.tree[idx] += (end - start + 1) * self.lazy[idx]
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
        
    def add(self, L, R, value, index=0):
        if not index: index = (0, len(self.arr)-1, 1)
        start, end, idx = index

        self.propagate(index)
    
        if R < start or L > end:
            return
        elif L <= start and R >= end:
            self.tree[idx] += (end - start + 1) * value
            if start != end:
                self.lazy[lc(idx)] += value
                self.lazy[rc(idx)] += value
            return
    
        mid = (start+end)//2
        self.add(L, R, value, (start, mid, lc(idx)))
        self.add(L, R, value, (mid+1, end, rc(idx)))
        self.tree[idx] = self.tree[lc(idx)] + self.tree[rc(idx)]
        
class MinSegmentTree:

    def __init__(self, arr, max_value):
        self.arr = arr
        self.size = len(arr)<<2
        self.tree = [max_value]*(self.size)
        self.lazy = [0]*(self.size)
        self.merge = lambda a, b: min(a, b)
        self.max_value = max_value
        segmentify(tree=self.tree, index=(0, len(self.arr)-1, 1), merge=self.merge, arr=self.arr)

    def propagate(self, index):
        start, end, idx = index
        if self.lazy[idx] != 0:
            self.tree[idx] += self.lazy[idx]
            if start != end:
                self.lazy[lc(idx)] += self.lazy[idx]
                self.lazy[rc(idx)] += self.lazy[idx]
            self.lazy[idx] = 0
    
    def min(self, L, R, index=0):
        if not index: index = (0, len(self.arr)-1 ,1)
        start, end, idx = index

        self.propagate(index)
    
        if R < start or L > end:
            return self.max_value
        elif L <= start and R >= end:
            return self.tree[idx]
        else:
            mid = (start+end)//2
            a = self.min(L, R, (start, mid, lc(idx)))
            b = self.min(L, R, (mid+1, end, rc(idx)))
            return self.merge(a, b)
        
    def add(self, L, R, value, index=0):
        if not index: index = (0, len(self.arr)-1, 1)
        start, end, idx = index

        self.propagate(index)
    
        if R < start or L > end:
            return
        elif L <= start and R >= end:
            self.tree[idx] += value
            if start != end:
                self.lazy[lc(idx)] += value
                self.lazy[rc(idx)] += value
            return
    
        mid = (start+end)//2
        self.add(L, R, value, (start, mid, lc(idx)))
        self.add(L, R, value, (mid+1, end, rc(idx)))
        self.tree[idx] = self.merge(self.tree[lc(idx)], self.tree[rc(idx)])
        
n, q = map(int, input().split())
arr = [*map(int, input().split())]

s1 = SumSegmentTree(arr)
s2 = MinSegmentTree(arr, 10**10)

for _ in range(q):
    p = input()
    if p[0] == 'S':
        a, b = map(int, p[2:].split())
        print(s1.sum(a-1, b-1))
    if p[0] == 'M':
        a, b = map(int, p[2:].split())
        print(s2.min(a-1, b-1))
    if p[0] == 'P':
        a, b, c = map(int, p[2:].split())
        s1.add(a-1, b-1, c)
        s2.add(a-1, b-1, c)
