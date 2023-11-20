from bisect import bisect_right

n = int(input())
    
p = []
    
for a1 in range(10):
    for a2 in range(10):
        for a3 in range(10):
            for a4 in range(10):
                for a5 in range(10):
                    s1 = str(a1)
                    s2 = str(a2)
                    s3 = str(a3)
                    s4 = str(a4)
                    s5 = str(a5)
                    
                    k1 = int(s1+s2+s3+s4+s5+s4+s3+s2+s1)
                    k2 = int(s1+s2+s3+s4+s5+s5+s4+s3+s2+s1)
                    
                    while k1 and not k1 % 10:
                        k1 //= 10
                        
                    while k2 and not k2 % 10:
                        k2 //= 10
                    
                    if k1: p.append(k1)
                    if 0 < k2 < 10**10: p.append(k2)
                    
p = sorted(p)

print(bisect_right(p, n))

