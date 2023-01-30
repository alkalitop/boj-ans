k = int(input())

line = {
    1: {
        'cnt': 0,
        'dis': []
    },
    2: {
        'cnt': 0,
        'dis': []
    },
    3: {
        'cnt': 0,
        'dis': []
    },
    4: {
        'cnt': 0,
        'dis': []
    }
}

s1 = 0
s2 = 0
t1 = 0
t2 = 0

seq = []

def prevnext (u):
    if u == 0:
        return (5, 1)
    elif u == 5:
        return (4, 0)
    else:
        return (u-1, u+1)

for i in range(6):
    n, d = map(int, input().split())
    line[n]['cnt'] += 1
    line[n]['dis'].append((i, d))
    seq.append(n)
    
    if line[n]['cnt'] == 2:
        if s1 == 0:
            s1 = n
            if n <= 2:
                t1 = 1 if s1 == 2 else 2
            else:
                t1 = 3 if s1 == 4 else 4
        else:
            s2 = n
            if n <= 2:
                t2 = 1 if s2 == 2 else 2
            else:
                t2 = 3 if s2 == 4 else 4

p1 = prevnext(line[s1]['dis'][0][0])
if line[s2]['dis'][0][0] in p1 and line[s2]['dis'][1][0] in p1:
    v_small = line[s1]['dis'][0][1]
else:
    v_small = line[s1]['dis'][1][1]

p2 = prevnext(line[s2]['dis'][0][0])
if line[s1]['dis'][0][0] in p2 and line[s1]['dis'][1][0] in p2:
    h_small = line[s2]['dis'][0][1]
else:
    h_small = line[s2]['dis'][1][1]

S_small = v_small*h_small
S_large = line[t1]['dis'][0][1] * line[t2]['dis'][0][1]



print(k * (S_large - S_small))
