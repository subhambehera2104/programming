#include <stdio.h>
int main()
{
	int n = 4;
	int num[]={4,5,1,2};
	int sum =0;
	for (int i = 0; i < n; i++)
	{
		sum=sum+num[i];
	}
	int avg =sum/n;
	printf("Avg is %d ", avg);
	return 0;
}