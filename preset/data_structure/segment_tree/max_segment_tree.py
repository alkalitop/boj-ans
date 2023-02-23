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
