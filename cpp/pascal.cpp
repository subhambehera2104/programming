#include <iostream>
#include <cmath>
#include <cstring>
using namespace std;

int main()
{
	int n=4;
	char result[10];
	for (int i = 0; i < n; i++)
	{
		for (int s = 0; s < (n-i); s++)
		{
			cout<<" ";
		}

	 sprintf(result, "%.0f", pow(11,i));

	  for( int j = 0; j < strlen(result); j++)
	     {
	    	cout<< result[j]<<" ";
	    }  
	     cout<<"\n";
	}
	return 0;
}