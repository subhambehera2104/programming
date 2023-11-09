#include<iostream>
using namespace std;

int main()
{
	int matrix1[2][2]={
		{6, 2},
		{5, 1}
	};
	int matrix2[2][1]={
		{4},
		{2}
	};

	int matrix1_rows=sizeof(matrix1)/sizeof(matrix1[0]);
	int matrix1_cols=sizeof(matrix1)/(matrix1_rows*sizeof(matrix1[0][0]));

	int matrix2_rows=sizeof(matrix2)/sizeof(matrix2[0]);
	int matrix2_cols=sizeof(matrix2)/(matrix2_rows*sizeof(matrix2[0][0]));

	if (matrix1_cols==matrix2_rows)
	{
		int mult_res[matrix1_rows][matrix2_cols];
		for (int i = 0; i < matrix1_rows; i++)
		{
			for (int j = 0; j < matrix2_cols; j++)
			{
				mult_res[i][j]=0;
				for (int k = 0; k < matrix2_rows; k++)
				{
					mult_res[i][j]+=(matrix1[i][k]*matrix2[k][j]);
				}
			
			     cout<<mult_res[i][j];
			}
			        cout<<"\n";
		}
	}
	else 
	{
		cout<<"order of matrices dose not match so multiplication of matrices not possible "		;
	}


	return 0;
} 