#include<iostream>
using namespace std;
int main()
{
	int num =65;
	int n=4;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n-i ; j++)
		{
			cout<<"  ";
		}	
		for (int k = i; k >=0; k--)
			{
				cout<<(char) (num+k) <<" ";
			}
		
				cout<<"\n";
	}
	
	return 0;
}