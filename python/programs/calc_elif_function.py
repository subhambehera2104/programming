def sum(x,y):
	return x+y

def sub(x,y):
	return x-y

def mul(x,y):
	return x*y
def div(x,y):
	if y != 0:
		return x/y
	else:
		return "Division by 0 not allowed"
def rem(x,y):
	if y !=0:
		return x%y
	else:
		return"Division by 0 not allowed"

# main

choice=int(input("Enter number 1-5 for \n1.sum \n 2.sub \n 3.mul \n 4.div \n 5.rem \n choice " ))
x=int(input("Enter number x "))
y=int(input("Enter number y "))
if choice == 1:
	 print(sum(x,y))
elif choice == 2:
	 print(sub(x,y))
elif choice == 3:
	 print(mul(x,y))
elif choice == 4:
	 print(div(x,y))
elif choice == 5:
	 print(rem(x,y))
else:
	print("invalid choice")

