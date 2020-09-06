# Enter your code here
def t1(a):
	if isinstance(a[0],str) and (len(a)==1):
		return True
	else:
		return False
def t2(a):
	if isinstance(a[0],list) and (len(a)==1):
		return True
	else:
		return False
def t3(a):
	if isinstance(a[0],str) and (len(a)>1):
		return True
	else:
		return False

def collapse(L):
	s = lambda l: l[0] if t1(l) else (s(l[0]) if t2(l) else (l[0]+' '+s(l[1:]) if t3(l) else s(l[0])+' '+s(l[1:])))
	return(s(L))