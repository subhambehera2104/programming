#include <stdio.h>
int main()
{
	int n=4;
	for (int i=0; i<=4; i++)
	{
		for (int j=0; j< i; j++)
		{
			printf(" ");	
		}
		for (int k=1; k<=4-i;k++)
		{
			printf("*");
		}
			printf("\n");
	}
	return 0;
}