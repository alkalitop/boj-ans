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

def segquery(tree, index, merge, arr=0, query=0, default):
    start, end, idx = index # 리스트 시작 인덱스, 리스트 끝 인덱스, 트리 인덱스
    L, R = interval # 합 시작, 합 끝
    
    if R < start or L > end:
        return outofrange
    elif L <= start and R >= end:
        return tree[idx]
    else:
        mid = (start+end)//2
        a = segsum(tree, (start, mid, idx<<1), (L, R))
        b = segsum(tree, (mid+1, end, (idx<<1)+1), (L, R))

class SumSegmentTree:

    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)<<2
        self.tree = [0]*(self.size)
        self.merge = lambda a,b: a+b
        segmentify(tree=self.tree, index=(0,(self.size>>2)-1,1), merge=self.merge, arr=self.arr)
        return self.tree
    
    def sum(self, L, R, index=(0,(self.size>>2)-1,1)):
        start, end, idx = index # 리스트 시작 인덱스, 리스트 끝 인덱스, 트리 인덱스
    
        if R < start or L > end:
            return 0
        elif L <= start and R >= end:
            return self.tree[idx]
        else:
            mid = (start+end)//2
            a = self.sum(self.tree, L, R, (start, mid, idx<<1))
            b = self.sum(self.tree, L, R, (mid+1, end, (idx<<1)+1))
            return self.merge(a, b)
        
    def update(self, target, value, index=(0,(self.size>>2)-1,1)):
        start, end, idx = index # 리스트 시작 인덱스, 리스트 끝 인덱스, 트리 인덱스
    
        if target < start or target > end: return
    
        tree[idx] += val
        if start == end: return
    
        mid = (start+end)//2
        self.update(tree, (start, mid, idx<<1), target, val)
        self.update(tree, (mid+1, end, (idx<<1)+1), target, val)
