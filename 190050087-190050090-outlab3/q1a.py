import argparse
from ring import RingInt

def fac(k,n):
	f=RingInt(n,1)
	for i in range(k,0,-1):
		f = f*RingInt(n,i);
	return(f)

def s1(k,x,n):
		if n<=k:
			raise ValueError('UNDEFINED')
		else:
			X = RingInt(n,x)
			sum = RingInt(n, 0)
			for i in range(0,k):
				fac = 1
				for j in range(i, 0, -1):
					fac = fac*j
				factorial = RingInt(n,fac%n)
				sum = sum+(X**i)/factorial
		return(sum)

def s2(k,x,n):
		if n<(x+k):
			raise ValueError('Undefined')
		else:
			X = RingInt(n,x)
			s = RingInt(n,1)
			for i in range(0,k):
				sum = RingInt(n,0)
				for j in range(0,i+1):
					sum = sum+(fac(x+i,n)/(fac(j,n)*fac(x+i-j,n)))
				s = s*sum

		return(s)

def s3(k,x,n):
	if n<=x or n<=k:
		raise ValueError('UNDEFINED')
	else:
		sum = RingInt(n,0)
		for i in range(1,k+1):
			sum = sum+(RingInt(n,i)**x)
		return(sum)# Enter your code here

parser = argparse.ArgumentParser()
parser.add_argument('-in', action="store", dest="inp")
parser.add_argument('-out', action="store", dest="out")
args = parser.parse_args()

inp = open(args.inp, 'r')
#lines=inp.readline()
#print(lines)
out = open(args.out, 'w')
for l in inp:
	k,x,n,s_no = map(int, l.split())
	if(s_no==1):
		try:
			out.write(str(s1(k,x,n))+'\n')
		except ValueError as ve:
			out.write('UNDEFINED'+'\n')
	if(s_no==2):
		try:
			out.write(str(s2(k,x,n))+'\n')
		except ValueError as ve:
			out.write('UNDEFINED'+'\n')
	if(s_no==3):
		try:
			out.write(str(s3(k,x,n))+'\n')
		except ValueError as ve:
			out.write('UNDEFINED'+'\n')

