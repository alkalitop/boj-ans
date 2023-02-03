def segmentify(tree, index, arr):
    start, end, idx = index # 리스트 시작 인덱스, 리스트 끝 인덱스, 트리 인덱스
    
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    
    mid = (start+end)//2
    tree[idx] = segmentify(arr, tree, (start, mid, idx<<1)) + segmentify(arr, tree, (mid+1, end, (idx<<1)+1))
    return tree[idx]
  
def segsum(tree, index, interval):
    start, end, idx = index # 리스트 시작 인덱스, 리스트 끝 인덱스, 트리 인덱스
    L, R = interval # 합 시작, 합 끝
    
    if R < start or L > end:
        return 0
    elif L <= start and R >= end:
        return tree[idx]
    else:
        mid = (start+end)//2
        return segsum(tree, (start, mid, idx<<1), (L, R)) + segsum(tree, (mid+1, end, (idx<<1)+1), (L, R))
      
def segupdate(tree, index, target, val):
    start, end, idx = index # 리스트 시작 인덱스, 리스트 끝 인덱스, 트리 인덱스
    
    if target < start or target > end: return
    
    tree[idx] += val
    if start == end: return
    
    mid = (start+end)//2
    update(tree, (start, mid, idx<<1), target, val)
    update(tree, (mid+1, end, (idx<<1)+1), target, val)
