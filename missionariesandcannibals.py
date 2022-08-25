from collections import deque

def BFS():
	path = []
	q = deque()
	q.append((3,3,0,0,0))
	path.append((3,3,0,0,0))
	pos_states = [(1,0), (0,1), (1,1), (2,0), (0,2)]
	while (len(q) > 0):
		u = q.popleft()
		if(u[2]==3 and u[3]==3 and u[4]==1):
		    break
		if(u[4] == 0):
		    for s in pos_states:
		        ml = u[0] - s[0]
		        cl = u[1] - s[1]
		        mr = u[2] + s[0]
		        cr = u[3] + s[1]
		        v = (ml,cl,mr,cr,1)
		        if(ml>=0 and cl>=0 and mr<=3 and cr<=3 and (ml==0 or ml>=cl) and (mr==0 or mr>=cr) and v not in path):
		            q.append(v)
		            path.append(v)
		elif(u[4] == 1):
		    for s in pos_states:
		        ml = u[0] + s[0]
		        cl = u[1] + s[1]
		        mr = u[2] - s[0]
		        cr = u[3] - s[1]
		        v = (ml,cl,mr,cr,0)
		        if(ml<=3 and cl<=3 and mr>=0 and cr>=0 and (ml==0 or ml>=cl) and (mr==0 or mr>=cr) and v not in path):
		            q.append(v)
		            path.append(v)
	sz = len(path)
	for i in range(sz):
	    print(path[i])

if __name__ == '__main__':
	BFS()
	
