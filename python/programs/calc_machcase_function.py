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
x=input("Enter number x")
y=input("Enter number y")
choice=input("Enter number 1-5 for 1.sum \n 2.sub \n 3.mul \n 4.div \n 5.rem \n" )
match choice:
	case 1:
			return sum(x,y)
	case 2:
			return sub(x,y)
	case 3:
			return mul(x,y)
	case 4:
			return div(x,y)
	case 5:
			return rem(x,y)
	case _:
			return"invalid choice"

