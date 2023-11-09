#include <iostream>
using namespace std;
	 int main()
	{
		int n=4;
		for (int i=0; i<4; i++)
		{
			for (int j = 0; j<(2*i); j++)
			{
				printf(" ");
			}
			for (int k = 1; k <4-i ; k++)
			{
				printf(" * ");
			}
			printf("\n");

		}
		return 0;
	}
