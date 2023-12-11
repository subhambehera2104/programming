#include<iostream>
#include<vector>

using namespace std;
int maximumArray(int num[], int n)
{
	int max=num[0];
	for (int i = 1; i < n; i++)
	{
		if(num[i]>max)
		{
			max=num[i];
		}
	}
	return max;
}

int maximumVector(vector<int> num, int n)
{
	int max=num[0];
	for (int i = 1; i < n; i++)
	{
		if(num[i]>max)
		{
			max=num[i];
		}
	}
	return max;
}
int main()
{
 int num[]={1, 2, 12, 31, 0};
 int n= sizeof(num)/sizeof(num[0]);
 int res= maximumArray(num, n);
 printf("array maximum is %d",res);

 printf("\n--------\n");

 vector<int> numVector{1, 2, 12, 31, 0};
 int n2= numVector.size();
 int res2= maximumVector(numVector, n2);
 printf("vector maximum is %d",res2);
}