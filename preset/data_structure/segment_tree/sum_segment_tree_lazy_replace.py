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
        self.lazy_trig = [0]*(self.size)
        self.lazy_value = [0]*(self.size)
        self.merge = lambda a,b: a+b
        segmentify(tree=self.tree, index=(0, len(self.arr)-1, 1), merge=self.merge, arr=self.arr)

    def prop(self, value, index):
        start, end, idx = index
        if start == end:
            self.tree[idx] = value
        else:
            self.lazy_trig[idx] = 1
            self.lazy_value[idx] = value
            self.tree[idx] = (end - start + 1) * value

    def sum(self, L, R, index=0):
        if not index: index = (0, len(self.arr)-1 ,1)
        start, end, idx = index
    
        if R < start or L > end:
            return 0
        elif L <= start and R >= end:
            return self.tree[idx]
        
        mid = (start+end)//2

        if self.lazy_trig[idx]:
            self.lazy_trig[idx] = 0
            self.prop(self.lazy_value[idx], (start, mid, lc(idx)))
            self.prop(self.lazy_value[idx], (mid+1, end, rc(idx)))
            self.lazy_value[idx] = 0

        a = self.sum(L, R, (start, mid, lc(idx)))
        b = self.sum(L, R, (mid+1, end, rc(idx)))
        return self.merge(a, b)
        
    def replace(self, L, R, value, index=0):
        if not index: index = (0, len(self.arr)-1, 1)
        start, end, idx = index

        if start == end:
            self.tree[idx] = value
    
        if R < start or L > end:
            return
        elif L <= start and R >= end:
            self.lazy_trig[idx] = 1
            self.lazy_value[idx] = value
            return
    
        mid = (start+end)//2

        if self.lazy_trig[idx]:
            self.lazy_trig[idx] = 0
            self.prop(self.lazy_value[idx], (start, mid, lc(idx)))
            self.prop(self.lazy_value[idx], (mid+1, end, rc(idx)))
            self.lazy_value[idx] = 0
        
        self.replace(L, R, value, (start, mid, lc(idx)))
        self.replace(L, R, value, (mid+1, end, rc(idx)))
        self.tree[idx] = self.merge(self.tree[lc(idx)], self.tree[rc(idx)])
