#include <stdio.h>

void sort_ascending(int num[], int n)
{
	printf("sort_ascending  ");
	for (int i = 0; i < n; i++)
	{
		for (int j = i+1; j < n; j++)
		{
			if (num[i]>num[j] )				
			{
				int temp=num[i];
				num[i]=num[j]; 
				num[j]=temp;		
			}
		}
		printf("%d, ", num[i]);
	}
}

void sort_descending(int num[], int n){
	printf("sort_descending  ");
	for (int i = 0; i < n; i++)
	{
		for (int j = i+1; j < n; j++)
		{
			if (num[i]<num[j] )				
			{
				int temp=num[i];
				num[i]=num[j]; 
				num[j]=temp;		
			}
		}
		printf("%d, ", num[i]);
	}
}

int main()
{
	// int num[4];
	// num[0]=2;
	// num[1]=5;
	// num[2]=1;
	// num[3]=10;

	int num[] = {2, 5, 1, 10};
	int n=sizeof(num)/ sizeof(num[0]);

	sort_ascending(num, n);
	printf("\n");
	sort_descending(num, n);
	
	return 0;
}