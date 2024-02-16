n=4
for i in range(0,n):
	for j in range(0,n-i):
		print(end="  ")
	for k in range(2*i+1,0,-2):
		print(k, end=" ")	
	print("\n")