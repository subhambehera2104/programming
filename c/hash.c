#include<stdio.h>
int main()
{
	int n, bucket;
	printf("Enter Number ");
	scanf("%d", &n);
	bucket = n%10;
	printf("Bucket is %d", bucket);
	return 0;
}