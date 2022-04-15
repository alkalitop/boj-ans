import sys
from bisect import bisect_left, bisect_right
bl = bisect_left
br = bisect_right
input = sys.stdin.readline

n = int(input())
arr = [0]*n

def arit (s):
    return round(sum(s)/len(s))

def median (s):
    return s[(n-1)//2]

def mode (s):
    elem = list(set(s))
    val = []
    freq = None
    for e in elem:
        if len(val) == 0:
            val.append(e)
            freq = br(s, e) - bl(s, e)
        else:
            tmp = br(s, e) - bl(s, e)
            if tmp > freq:
                val = [e]
                freq = tmp
            elif tmp == freq:
                val.append(e)
    val.sort()
    return val[1 if len(val) > 1 else 0]

def rang (s):
    return max(s) - min(s)

for i in range(n):
    arr[i] = int(input())
arr.sort()

print(arit(arr))
print(median(arr))
print(mode(arr))
print(rang(arr))
