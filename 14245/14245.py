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

class XORSegmentTree:

    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)<<2
        self.tree = [0]*(self.size)
        self.lazy = [0]*(self.size)
        self.merge = lambda a,b: a^b
        segmentify(tree=self.tree, index=(0, len(self.arr)-1, 1), merge=self.merge, arr=self.arr)

    def propagate(self, index):
        start, end, idx = index
        if self.lazy[idx] != 0:
            self.tree[idx] = self.tree[idx] ^ (self.lazy[idx] if (end - start + 1) & 1 else 0) 
            if start != end:
                self.lazy[lc(idx)] = self.lazy[lc(idx)] ^ self.lazy[idx]
                self.lazy[rc(idx)] = self.lazy[rc(idx)] ^ self.lazy[idx]
            self.lazy[idx] = 0
    
    def iv_xor(self, L, R, index=0):
        if not index: index = (0, len(self.arr)-1 ,1)
        start, end, idx = index

        self.propagate(index)
    
        if R < start or L > end:
            return 0
        elif L <= start and R >= end:
            return self.tree[idx]
        else:
            mid = (start+end)//2
            a = self.iv_xor(L, R, (start, mid, lc(idx)))
            b = self.iv_xor(L, R, (mid+1, end, rc(idx)))
            return self.merge(a, b)
        
    def ap_xor(self, L, R, value, index=0):
        if not index: index = (0, len(self.arr)-1, 1)
        start, end, idx = index

        self.propagate(index)
    
        if R < start or L > end:
            return
        elif L <= start and R >= end:
            self.tree[idx] = self.tree[idx] ^ (value if (end - start + 1) & 1 else 0)
            if start != end:
                self.lazy[lc(idx)] = self.lazy[lc(idx)] ^ value
                self.lazy[rc(idx)] = self.lazy[rc(idx)] ^ value
            return
    
        mid = (start+end)//2
        self.ap_xor(L, R, value, (start, mid, lc(idx)))
        self.ap_xor(L, R, value, (mid+1, end, rc(idx)))
        self.tree[idx] = self.merge(self.tree[lc(idx)], self.tree[rc(idx)])
        
n = int(input())
s = XORSegmentTree([*map(int, input().split())])
for _ in range(int(input())):
    q = input()
    if q[0] == '1':
        s.ap_xor(*map(int, q[2:].split()))
    else:
        print(s.iv_xor(int(q[2:]), int(q[2:])))
