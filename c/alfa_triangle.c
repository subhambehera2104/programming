#include <stdio.h>
int main()
{
	int num=65;
	int n=4;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n-i; j++)
		{
			printf(" ");
		}
		for (int k = i; k >=0; k--)
		{
			
			printf("%c",num+k);
		}
			printf("\n");
	}
	return 0;
}