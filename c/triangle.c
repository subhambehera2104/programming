#include <stdio.h>
int main()
{
	int n=3;
	for (int i = 0; i <n; i++)
	{
		for (int j = 1; j <n-i ; j++)
		{
			printf(" ");
		}
		for (int k = 0; k <i+1 ; k++)
		{
			printf("* ");
		}
			printf("\n");
	}
	return 0;
}