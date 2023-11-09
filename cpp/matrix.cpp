#include<iostream>
using namespace std;

int main()
{
	int matrix[3][4]={
		{1,2,3,4},
		{5,6,7,8},
		{9,1,2,5},
	};
	int rows=sizeof(matrix)/sizeof(matrix[0]);
	int cols=sizeof(matrix)/(rows*sizeof(matrix[0][0]));   
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++)
		{
			cout<<matrix[i][j]<<" ";
		}
			cout<<"\n";
	}
    return 0;
}