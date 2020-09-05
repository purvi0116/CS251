# Enter your code here
class RingInt:
	def __init__(self, characteristic, value):
		self.char = int(characteristic)
		self.value=int(value)

	def __str__(self):
		return(str(self.value)+'['+str(self.char)+']')

	def __add__(self,other):
		if self.char == other.char:
			obj  = RingInt(self.char, (self.value+other.value)%self.char)
			return(obj)
		else:
			raise ValueError('UNDEFINED')

	def __mul__(self, other):
		if self.char == other.char:
			obj  = RingInt(self.char, (self.value*other.value)%self.char)
			return(obj)
		else:
			raise ValueError('UNDEFINED')

	def __sub__(self, other):
		if self.char == other.char:
			obj  = RingInt(self.char, abs(self.value%self.char - other.value%self.char)%self.char)
			return(obj)
		else:
			raise ValueError('UNDEFINED')

	def __truediv__(self, other):
		if self.char == other.char and other.value%self.char !=0 :

			x = self.char
			y = other.value
			if x > y: 
				small = y
			else: 
				small = x
			for i in range(1, small+1):
				if((x % i == 0) and (y % i == 0)):
					gcd = i
			if gcd!=1:
				raise ValueError('UNDEFINED')

			for i in range(self.char):
				if (other.value*i)%self.char == self.value%self.char:
					obj  = RingInt(self.char, i)
					return(obj)

		else:
			raise ValueError('UNDEFINED')

	def __pow__(self, exp):
		obj  = RingInt(self.char, pow(self.value%self.char, exp%self.char)%self.char)
		return(obj)

	def __eq__(self, other):
		if self.char == other.char:
			return(RingInt(self.char, self.value%self.char == other.value%self.char))
		else:
			raise ValueError('UNDEFINED')