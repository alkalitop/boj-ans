x,y=map(int,input().split());print('BA'[x&1&-~y&1|(x-y)%(2*(x&-x))and 1],'player wins')
