n=4
for i in range(0,n):
	for s in range(0,(n-i)):
		print(end=" ")
	
	res = str(11**i)
	for j in range(len(res)):
		print(res[j], end=" ")
	print("\n")
