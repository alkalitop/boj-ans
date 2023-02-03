def segmentify(tree, index, arr):
    start, end, idx = index # 리스트 시작 인덱스, 리스트 끝 인덱스, 트리 인덱스
    
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    
    mid = (start+end)//2
    tree[idx] = segmentify(tree, (start, mid, idx<<1), arr) + segmentify(tree, (mid+1, end, (idx<<1)+1), arr)
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
    segupdate(tree, (start, mid, idx<<1), target, val)
    segupdate(tree, (mid+1, end, (idx<<1)+1), target, val)

n, m, k = map(int, input().split())
A = [0]*n
segtree = [0]*(n*4)

initindex = (0, n-1, 1)

for i in range(n):
    A[i] = int(input())

segmentify(tree=segtree, index=initindex, arr=A)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        c -= A[b]
        segupdate(tree = segtree, index=initindex, target=b, val=c)
        A[b] += c
    if a == 2:
        b -= 1
        c -= 1
        print(segsum(tree = segtree, index=initindex, interval=(b, c)))
