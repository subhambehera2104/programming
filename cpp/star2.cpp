#include <iostream>
using namespace  std;
void starPattern2(int n){
	for (int i = 0; i < n; i++)
		{
			for (int j = 0; j<=i; j++)
			{
				printf("*");
			}
			printf("\n");
		}	
}
int main()
{
	int n=4;
	starPattern2(n);	
	return 0;
}