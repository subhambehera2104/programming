matrix_1 =[
  [6, 2, 4],
  [1, 2, 3]
]
matrix_2=[
  [4],
  [2],
  [1]
]
matrix1_rows=len(matrix_1)
matrix1_cols=len(matrix_1[0])

matrix2_rows=len(matrix_2)
matrix2_cols=len(matrix_2[0])

mult_res = []
for i in range(matrix1_rows):
	row = []
	for j in range(matrix2_cols):
		row.append(0)
	mult_res.append(row)

if matrix1_cols==matrix2_rows:

	for i in range(0,matrix1_rows):
		for j in range(0,matrix2_cols):
			mult_res[i][j]=0
			for k in range(0,matrix2_rows):
				mult_res[i][j]+=matrix_1[i][k]*matrix_2[k][j]
			print(mult_res[i][j], end="")
		print("\n")
	
else:
	print("order of matrices dose not match so multiplication of matrices not possible")