#include <stdio.h>
int main()
{
	int n =4;
	int num[n];
	float  sum=0;
	for (int i = 0; i < n; i++)
	{	printf("enter num %d \n",i);
		scanf("%d",& num[i]);
		sum=sum+num[i];

	}
		printf("Avg is %f ", (sum/n));
	return 0;
}