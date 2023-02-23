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
