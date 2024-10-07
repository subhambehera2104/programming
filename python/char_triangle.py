num = 65
n = 4
for i in range(0,n):
	for j in range(0,i+1):
		print(chr(num+j), end=" ")
	print("\n")