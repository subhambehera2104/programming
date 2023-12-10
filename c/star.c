#include <stdio.h>

void starPattern(int n){
	for (int i = 0; i<n;i++)
	{
		for (int j=0 ; j<n ; j++)
		{
			printf("*");
		}
		printf("\n");
	}

}
int main()
{
	int n=4;
    starPattern(n);
	return 0;
}