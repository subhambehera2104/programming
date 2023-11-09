#include <stdio.h>
#include <string.h>
#include <math.h>

// gcc pascal.c -lm 
// link math library

int main()
{
	int n=4;
	char result[10];
	for (int i = 0; i < n; i++)
	{
		for (int s = 0; s < (n-i); s++)
		{
			printf(" ");
		}

	  sprintf(result, "%.0f", pow(11,i));
	  for( int j = 0; j < strlen(result); j++)
	     {
	    	printf("%c ",result[j]);
	    }  
	     printf("\n");
	}
	return 0;
}