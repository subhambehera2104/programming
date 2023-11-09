#include <stdio.h>
int main()
{
	int n = 4;
	int num[]={4,5,1,2};
	float sum =0;
	for (int i = 0; i < n; i++)
	{
		 sum=sum+num[i];
	}
	int avg =sum/n;
	printf("Avg is %f ", avg);
	return 0;
}