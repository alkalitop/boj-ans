import math

n = int(input())
m = int(input())

vertex = [math.inf]*n
edge = []

for _ in range(m):
    p, q, r = map(int, input().split())
    edge.append((p-1, q-1, r))

a, b = map(int, input().split())
vertex[a-1] = 0

unvisited = [i for i in range(n)]
cur = a-1

unvisited.remove(cur)

def set_weight(e):
    vertex[e[1]] = min(vertex[e[0]] + e[2], vertex[e[1]])

def next():
    global cur
    cur = unvisited[0]
    for v in unvisited:
        if vertex[v] < vertex[cur]:
            cur = v
    unvisited.remove(cur)
            
while len(unvisited):
    for e in edge:
        if e[0] == cur and e[1] in unvisited:
            set_weight(e)
    next()

print(vertex[b-1])
