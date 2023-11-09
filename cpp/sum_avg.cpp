#include<iostream>
using namespace std;

int main()
{
	int n=4;
	 float num[]={5,4,3,2};
	 float sum=0;
	 for (int i = 0; i < n; i++)
	 {
	 	sum=sum+num[i];
	 }
	 float avg=sum/n;
	 cout<<"Avg is "<<avg;
	return 0;
}