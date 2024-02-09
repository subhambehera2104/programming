#include<stdio.h>
int main()
{
int num[] = {15, 1, 4, 6, 7, 8, 12};
int search=8;
int found = 0;
int n = sizeof(num)/sizeof(num[0]);
for(int i = 0; i < n; i++)
 {
 	if(search==num[i])
 	{
     printf("Found at index %d",i);
     found = 1; 
 	break; 
 	}
 	
 }
 if(found==0)
 	{
 		printf("Not found");
 	}
	return 0;
}