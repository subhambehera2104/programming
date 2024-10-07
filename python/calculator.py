class Calculatar:
	"""docstring for calculatar"""
	def __init__(self):
		self.result=0
	def  add(self,x,y):
		self.result=x+y
		return self.result
	def sub(self,x,y):
		self.result=x-y
		return self.result

# main
x=7
y=1
c=Calculatar()
sum = c.add(x,y)
print(f"sum is {sum}")
sub = c.sub(x,y)
print(f"sub is {sub}")