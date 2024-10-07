matrix=[
 [3, 2, 1],
 [4, 5, 6]
]

matrix_rows=(len(matrix))
matrix_cols=(len(matrix[0]))
matrix_res=[]
for j in range(matrix_cols):
 	rows_list=[]
 	for i in range(matrix_rows):
 		rows_list.append(0)
 	matrix_res.append(rows_list)


for i in range(matrix_cols):
	for j in range(matrix_rows):
		matrix_res[i][j]=matrix[j][i]
		print(matrix_res[i][j], end="  ")
	print("\n")	