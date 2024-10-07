matrix=[
[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
]
rows=len(matrix)
cols=len(matrix[0])
for i in range(0,rows):
	for j in range(0,cols):
		print(f"{matrix[i][j]}", end=" ")
	print("\n")