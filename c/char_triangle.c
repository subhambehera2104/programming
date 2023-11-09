#include <stdio.h>
int main()
{
	int num=65;
	int n=10;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < i+1; j++)
		{
			printf("%c",num+j);
		}
			printf("\n");
	}
	return 0;
} 