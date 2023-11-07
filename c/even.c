#include <stdio.h>
int main()
{
	int num,remainder;
	printf("enter number ");
	scanf("%d",&num);
	remainder=num%2;

	if (remainder==0)
	{
		printf("%d is even",num);
	}
	else
	{
		printf("%d is odd",num);
	}
	
	return 0;
}