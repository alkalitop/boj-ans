s=[input().split() for i in range(20)]
t=['F','P','D0','D+','C0','C+','B0','B+','A0','A+']
print(sum(map(lambda a:(float(a[1]) if a[2]!='P' else 0)*(t.index(a[2])/2),s))/sum(map(lambda a:float(a[1]) if a[2]!='P' else 0,s)))
