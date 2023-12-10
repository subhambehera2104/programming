#include <iostream>
using namespace std;

void reverseMatrix(int matrix[][3]){
	
    int matrixRows=(sizeof(matrix)/sizeof(matrix[0]));
    int matrixCols=(sizeof(matrix)/(matrixRows*sizeof(matrix[0][0])));
    cout<<"rows  cols \n",matrixRows,matrixCols ;
	int matrixRes[matrixCols][matrixRows];

	for(int i = 0; i < matrixCols; i++)
	{
	  for(int j =0; j< matrixRows; j++)
	  {
		 matrixRes[i][j]=matrix[j][i];
		 cout<< matrixRes[i][j];
	  }
	  cout<<("\n");
	}



} 

int main()
{
	int matrix[2][3]={
		{3, 2, 1},
		{4, 5, 6}
	};

	reverseMatrix(matrix);
	return 0;
}