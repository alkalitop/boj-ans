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
  
  
class IndexedMinSegmentTree:
    
    def __init__(self, arr, max_value):
        self.arr = arr
        self.size = len(arr)<<2
        self.tree = [(max_value, self.size>>2)]*(self.size)
        def merge (a, b):
            if a[0] == b[0]:
                return (a[0], min(a[1], b[1]))
            elif a[0] < b[0]:
                return a
            else:
                return b
        self.merge = merge
        self.max_value = max_value
        segmentify(tree=self.tree, index=(0,(self.size>>2)-1,1), merge=self.merge, arr=self.arr)
    
    def min(self, L, R, index=0):
        if not index: index = (0,(self.size>>2)-1,1)
        start, end, idx = index # 리스트 시작 인덱스, 리스트 끝 인덱스, 트리 인덱스
    
        if R < start or L > end:
            return (self.max_value, self.size>>2)
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
            self.arr[target] = (value, target)
            self.tree[idx] = (value, target)
            return self.tree[idx]
    
        mid = (start+end)//2
        a = self.replace(target, value, (start, mid, idx<<1))
        b = self.replace(target, value, (mid+1, end, (idx<<1)+1))
        
        self.tree[idx] = self.merge(a, b)
        return self.tree[idx]    
