def segmentify(tree, index, merge, arr):
    start, end, idx = index # 리스트 시작 인덱스, 리스트 끝 인덱스, 트리 인덱스
    
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    
    mid = (start+end)//2
    a = segmentify(tree, (start, mid, idx<<1), merge, arr)
    b = segmentify(tree, (mid+1, end, (idx<<1)+1), merge, arr)
    tree[idx] = merge(a, b)
    return tree[idx]

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
        
class MinSegmentTree:
    
    def __init__(self, arr, max_value):
        self.arr = arr
        self.size = len(arr)<<2
        self.tree = [max_value]*(self.size)
        self.merge = lambda a,b: min(a, b)
        self.max_value = max_value
        segmentify(tree=self.tree, index=(0,(self.size>>2)-1,1), merge=self.merge, arr=self.arr)
    
    def min(self, L, R, index=0):
        if not index: index = (0,(self.size>>2)-1,1)
        start, end, idx = index # 리스트 시작 인덱스, 리스트 끝 인덱스, 트리 인덱스
    
        if R < start or L > end:
            return self.max_value
        elif L <= start and R >= end:
            return self.tree[idx]
        else:
            mid = (start+end)//2
            a = self.min(L, R, (start, mid, idx<<1))
            b = self.min(L, R, (mid+1, end, (idx<<1)+1))
            return self.merge(a, b)
        
    def replace(self, target, value, index=0):
        if not index: index = (0,(self.size>>2)-1,1)
        start, end, idx = index # 리스트 시작 인덱스, 리스트 끝 인덱스, 트리 인덱스
    
        if target < start or target > end: return self.tree[idx]
    
        if start == end: 
            self.arr[target] = value
            self.tree[idx] = value
            return self.tree[idx]
    
        mid = (start+end)//2
        a = self.replace(target, value, (start, mid, idx<<1))
        b = self.replace(target, value, (mid+1, end, (idx<<1)+1))
        
        self.tree[idx] = self.merge(a, b)
        return self.tree[idx]

class MaxSegmentTree:
    
    def __init__(self, arr, min_value):
        self.arr = arr
        self.size = len(arr)<<2
        self.tree = [min_value]*(self.size)
        self.merge = lambda a,b: max(a, b)
        self.min_value = min_value
        segmentify(tree=self.tree, index=(0,(self.size>>2)-1,1), merge=self.merge, arr=self.arr)
    
    def max(self, L, R, index=0):
        if not index: index = (0,(self.size>>2)-1,1)
        start, end, idx = index # 리스트 시작 인덱스, 리스트 끝 인덱스, 트리 인덱스
    
        if R < start or L > end:
            return self.min_value
        elif L <= start and R >= end:
            return self.tree[idx]
        else:
            mid = (start+end)//2
            a = self.max(L, R, (start, mid, idx<<1))
            b = self.max(L, R, (mid+1, end, (idx<<1)+1))
            return self.merge(a, b)
        
class MinMaxSegmentTree:
    
    def __init__(self, arr, min_value, max_value):
        self.arr = arr
        self.size = len(arr)<<2
        self.tree = [(max_value, min_value)]*(self.size) # 0번인덱스: 최소, 1번인덱스: 최대
        self.merge = lambda a,b: (min(a[0], b[0]), max(a[1], b[1]))
        self.min_value = min_value
        self.max_value = max_value
        segmentify(tree=self.tree, index=(0,(self.size>>2)-1,1), merge=self.merge, arr=self.arr)
    
    def minmax(self, L, R, index=0):
        if not index: index = (0,(self.size>>2)-1,1)
        start, end, idx = index # 리스트 시작 인덱스, 리스트 끝 인덱스, 트리 인덱스
    
        if R < start or L > end:
            return (self.max_value, self.min_value)
        elif L <= start and R >= end:
            return self.tree[idx]
        else:
            mid = (start+end)//2
            a = self.minmax(L, R, (start, mid, idx<<1))
            b = self.minmax(L, R, (mid+1, end, (idx<<1)+1))
            return self.merge(a, b)
