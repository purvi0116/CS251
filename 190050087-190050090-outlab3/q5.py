# Enter your code here
import time

def rotate(m):
	#reverse the outer list so that last list becomes 1st and 1st bms last and so on
	rev = list()
	n=len(m)
	ele = []
	for k in range(n):
		rev.append(m[n-1-k])
	for i in range(n):
		e=[sublist[i] for sublist in rev]
		ele.append(e)	
	return ele	
	
