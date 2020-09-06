from ring import *

def factorial(n,i):
	fac = RingInt(n,1)
	for k in range(i,0,-1):
		fac = fac*RingInt(n,k)
	return fac	

class Series:

	# Write your code here
	def __init__(self,k,x,n):
		self.k = int(k)
		self.x = int(x)
		self.n = int(n)
		self.i=0
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.i >=self.k:
			raise StopIteration
		S = RingInt(self.n,0)
		num = RingInt(self.n,self.x**self.i)
		den = factorial(self.n,self.i)
		S=num/den	
		self.i+=1
		return S
				

def main():

	in_str = str(input())
	in_list = in_str.split(' ')
	k, x, n = in_list[0], in_list[1], in_list[2]
	
	for ele in Series(k, x, n):
		print(ele)


if __name__=="__main__":
	main()

