#include<stdio.h>
int main()
{
	int matrix1[2][3]={
		{3, 2, 5},
		{1, 3, 6}
	   };
	int matrix2[2][4]={
		{3, 2, 1},
		{3, 2, 3}
	   };
	int matrix1_rows=sizeof(matrix1)/sizeof(matrix1[0]);
	int matrix1_cols=sizeof(matrix1)/(matrix1_rows*sizeof(matrix1[0][0]));

	int matrix2_rows=sizeof(matrix2)/sizeof(matrix2[0]);
	int matrix2_cols=sizeof(matrix2)/(matrix2_rows*sizeof(matrix2[0][0]));
		if (matrix1_rows==matrix2_rows && matrix1_cols==matrix2_cols)
		{
			int sum_matrix[matrix1_rows][matrix1_cols];
	for (int i = 0; i < matrix1_rows; i++)
	{
		for (int j = 0; j < matrix1_cols; j++)
		{
		printf("%d ",sum_matrix[i][j]=matrix1[i][j]+matrix2[i][j]);
		}
			printf("\n");
	}
		}
		 else 
		 {
		 	printf("order of matrices dose not mach");
		 }
		
    
    return 0;
}