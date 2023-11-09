#include <stdio.h>
int main()
{
	int num[]={4, 5, 1, 2, 6};

	printf("array total size in bytes %d \n",sizeof(num) );
	printf("array 0th element size in bytes %d \n",sizeof(num[0]) );

	int n = sizeof(num)/sizeof(num[0]);
	for (int i = 0; i < n; i++)
	{
		printf("%d ", num[i]);
	}
	
}