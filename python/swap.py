def swap1(x, y):
	temp=y
	y=x
	x=temp
	return x, y

def swap2(x, y):
	z=x+y
	y=z-y
	x=z-x
	return x, y



# main
x=2
y=3
x,y = swap1(x, y)
print("swap1")
print(f"x is {x}")
print(f"y is {y}")

x=2
y=3
x,y = swap2(x, y)
print("swap1")
print(f"x is {x}")
print(f"y is {y}")

x=2
y=3
x,y = y,x
print("swap3")
print(f"x is {x}")
print(f"y is {y}")