n = int(input())

stk = []
A = [i+1 for i in range(n)]

def list_find(li, el):
	try:
		return li.index(el)
	except:
		return -1

def push(k):
    u = list_find(A, k)
    for i in range(u+1):
        stk.append(A[i])
    for i in range(u+1):
    	del A[0]
    return u+1

def pop(k):
    if stk[-1] == k:
    	stk.pop()
    	return 1
    else:
    	return -1

query = []
pos = True

for i in range(n):
	k = int(input())
	push_cnt = push(k)
	pop_cnt = pop(k)
	if pop_cnt < 0:
		print('NO')
		pos = False
		break
	else:
		query += ['+']*push_cnt
		query += ['-']*pop_cnt
		
if pos:
	print('\n'.join(query))
		
